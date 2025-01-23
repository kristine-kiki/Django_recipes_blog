from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Category, Recipe
from .forms import RecipeForm


# Create your views here.
class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = 'recipes'
    paginate_by = 5

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
    results = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(ingredients__icontains=query)
    
    return render(
        request,
        'recipes/search_results.html',
        {
            'results': results
        }
    )

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    return render(
        request,
        'recipes/recipe_detail.html',
        {
            'recipe': recipe
        }
    )