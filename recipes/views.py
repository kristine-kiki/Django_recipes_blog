from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from .models import Category, Recipe, Rating
from .forms import RecipeForm, RatingForm, CommentForm
import math


# Create your views here.

def home(request):
    recipes = Recipe.objects.all().order_by('-created_on')[:6]
    for recipe in recipes:
        recipe.average_rating = recipe.ratings.aggregate(Avg('rating'))['rating__avg']
    return render(
        request, 'home.html', 
        {
            'recipes': recipes
        }
    )

class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 6

def recipe_list(request):
    recipes = Recipe.objects.all()
    paginator = Paginator(recipes,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "recipes/recipe_list.html",
        {
            "page_obj": page_obj
        }
    )

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit= False)
            recipe_user = request.user
            recipe.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe added!')
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    
    return render(
        request,
        'recipes/add_recipe.html',
        {
            'form': form
        }
    )

@login_required
def recipe_edit(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Ensure form is always defined
    form = RecipeForm(instance=recipe)

    if request.method == 'POST':
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        
        if recipe.user != request.user:
            messages.add_message(request, messages.ERROR, 'You do not have permission to edit this recipe!')
            return redirect('recipe_detail', recipe_id=recipe_id)

        if recipe_form.is_valid():
            recipe_form.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe updated successfully!')
            return redirect('recipe_detail', recipe_id=recipe.id)
        else:
            # If form is invalid, redefine it to show errors
            form = recipe_form

    return render(
        request,
        'recipes/recipe_edit.html',
        {
            'form': form,
            'recipe': recipe
        }
    )

def delete_recipe(request, id):
    # Get the recipe object or return a 404 error if not found
    recipe = get_object_or_404(Recipe, id=id)

    # Check if the current user is the owner of the recipe
    if recipe.user != request.user:
        messages.error(request, "You are not authorized to delete this recipe.")
        return redirect('recipe_detail', id=id)

    # Delete the recipe
    recipe.delete()
    
    # Display a success message
    messages.success(request, "Recipe deleted successfully.")

    # Redirect to the list of recipes or wherever appropriate
    return redirect('recipe_list')

class RecipeDetail(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = 'recipe'

def search(request):
    query = request.GET.get('query')
    if query:
        results = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(ingredients__icontains=query)
    else:
        results = Recipe.objects.none()
    return render(
        request,
        'recipes/search_results.html',
        {
            'results': results
        }
    )

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    comments = recipe.comments.all()
    ratings = recipe.ratings.all()
    user_rating = ratings.filter(user=request.user).first() if request.user.is_authenticated else None

    # Initialize forms
    rating_form = RatingForm()  # If you have a form to handle rating submissions
    comment_form = CommentForm()  # Initialize the comment form
    rating_range = [1, 2, 3, 4, 5]  # A range of rating options (1 to 5)

    # Handle POST requests (rating and comment submission)
    if request.method == "POST":
        if "rating_submit" in request.POST:  # Handle rating submission
            rating_value = request.POST.get("rating")
            if rating_value:
                # Save the rating to the database
                rating_value = int(rating_value)
                user_rating, created = Rating.objects.update_or_create(
                    user=request.user, recipe=recipe, defaults={'rating': rating_value}
                )

                if created:
                    messages.success(request, "Your rating has been submitted!")
                else:
                    messages.info(request, "Your rating has been updated!")
                return redirect("recipe_detail", recipe_id=recipe_id)

        elif "comment_submit" in request.POST:  # Handle comment submission
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.recipe = recipe
                comment.save()
                messages.success(request, "Your comment has been added!")
                return redirect("recipe_detail", recipe_id=recipe_id)

    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "ratings": ratings,
            "user_rating": user_rating,
            "rating_form": rating_form,
            "comment_form": comment_form,
            "rating_range": rating_range,
        },
    )

'''
@login_required
def add_rating(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        if 'rating' in request.POST:
            form = RatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.recipe = recipe
                rating.user = request.user
                rating.save()
                messages.add_message(request, messages.SUCCESS, 'Rating posted!')
        else:
            messages.add_message(request, messages.ERROR, 'Error posting rating!')
        return HttpResponseRedirect(reverse('recipe_detail', args=[recipe_id]))

@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment posted!')
        else:
            messages.add_message(request, messages.ERROR, 'Error posting comment!')
        return HttpResponseRedirect(reverse('recipe_detail', args=[recipe_id]))

    comment_form = CommentForm()
    return render(
        request, 
        'recipes/recipe_detail.html', 
        {
            'recipe': recipe,
            'comment_form': comment_form,
            'average_rating': recipe.average_rating()
        }
    )

'''