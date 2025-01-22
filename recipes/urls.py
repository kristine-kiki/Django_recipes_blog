from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipe_list'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('search/', views.search, name='search'),
    path('recipe/', views.recipe_list, name="recipe_list"),
]