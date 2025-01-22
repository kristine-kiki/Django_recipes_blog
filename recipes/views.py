from django.shortcuts import render, redirect
from django.views import generic
from .models import Category, Recipe
from .forms import RecipeForm


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = "recipes/recipe_list.html"
    paginate_by = 5

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

