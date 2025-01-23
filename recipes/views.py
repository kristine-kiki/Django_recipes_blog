from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from .models import Category, Recipe, Rating
from .forms import RecipeForm
from .forms import RatingForm
import math


# Create your views here.
class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 6

    #queryset = Recipe.objects.all()
    #template_name = "recipes/recipe_list.html"
    #paginate_by = 5

def recipe_list(request):
    recipes = Recipe.objects.all()

    return render(
        request,
        "recipes/recipe_list.html",
        {
            "recipes":recipes
        }
    )
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    
    return render(
        request,
        'recipes/add_recipe.html',
        {
            'form': form
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
    recipe = get_object_or_404(Recipe, id=recipe_id)
    form = RatingForm()
    rating_range = range(1, 6)  # Define the range here
    average_rating = recipe.ratings.aggregate(Avg('rating'))['rating__avg']  # Calculate the average rating
    if average_rating is not None:
        average_rating = round(average_rating, 1)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.recipe = recipe
            rating.user = request.user
            rating.save()
            return redirect('recipe_detail', recipe_id=recipe.id)

    return render(
        request, 
        'recipes/recipe_detail.html', 
        {
        'recipe': recipe,
        'form': form,
        'rating_range': rating_range,
        'average_rating': average_rating
    })