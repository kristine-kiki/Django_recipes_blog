from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add/', views.add_recipe, name='add_recipe'),  # Add recipe
    path('recipe/<int:recipe_id>/edit', views.recipe_edit, name='recipe_edit'),  # Edit a recipe
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Recipe details
    path('recipes/', views.recipe_list, name='recipe_list'),  # Recipe list using CBV
    path('recipe/<int:id>/delete/', views.delete_recipe, name='delete_recipe'),
    path('my_recipes/', views.my_recipes, name='my_recipes'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('search/', views.search, name='search'),  # Search page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
