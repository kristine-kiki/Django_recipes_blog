from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('search/', views.search, name='search'),
    
]