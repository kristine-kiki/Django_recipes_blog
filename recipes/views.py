import math

from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate, views as auth_views
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Comment
from django.views.generic import ListView, DetailView

from .models import Category, Recipe, Rating
from .forms import RecipeForm, RatingForm, CommentForm

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(status='approved').order_by('-created_on')[:6]
    for recipe in recipes:
        recipe.average_rating = recipe.ratings.aggregate(Avg('rating'))['rating__avg']
    return render(
        request, 'home.html', 
        {
            'recipes': recipes,
        }
    )

class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 6

def recipe_list(request):
    # Fetch approved recipes and original recipes awaiting editing approval
    recipes = Recipe.objects.filter(status='approved')
    for recipe in recipes:
        print(recipe.image.url)
    paginator = Paginator(recipes, 6)  # Paginate by 6 recipes per page
    page_number = request.GET.get('page')  # Get the current page number
    page_obj = paginator.get_page(page_number)  # Paginate the query
    

    return render(
        request,
        "recipes/recipe_list.html",
        {
            "page_obj": page_obj, # Pass the paginated recipes to the template  
        }
    )

@login_required(login_url='account_login')
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.status = 'pending'
            recipe.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe submitted for approval!')
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
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe_edited = form.save(commit=False)
            recipe_edited.status = 'pending'
            recipe_edited.parent = recipe  # Link the edited version to the original recipe
            recipe_edited.save()
            messages.add_message(request, messages.SUCCESS, 'Edition submitted for approval')
            return redirect('my_recipes')
    else:
        form = RecipeForm(instance=recipe)

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

@login_required
def my_recipes(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(
        request,
        'recipes/my_recipes.html',
        {
            'recipes': recipes,
        }
    )

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
    recipe = get_object_or_404(Recipe, id=recipe_id, status__in=['approved', 'pending'])
    comments = Comment.objects.filter(recipe=recipe, status='approved')  # Show only approved comments
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
                messages.success(request, "Your comment waiting for approval!")
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

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # After the user is created, you can redirect them to the login page or the home page
            return redirect('account_login')  # Redirect to the login page
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')  # Redirect to the homepage after logout
    return render(request, 'registration/logout.html')

