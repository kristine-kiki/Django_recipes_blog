from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('search/', views.search, name='search'),
    path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
    
]