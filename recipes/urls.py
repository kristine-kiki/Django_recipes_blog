from django.urls import path #import path function to define URL patterns
from django.contrib.auth import views as auth_views #import Djngo`s built-in auth views
from django.conf.urls.static import static #import static function to serve static files during development
from django.conf import settings #import settings to access project settings
from . import views #imort views from the current package

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add_recipe/', views.add_recipe, name='add_recipe'),  # Add recipe,
    path('recipe/<int:recipe_id>/edit', views.recipe_edit, name='recipe_edit'),  # Edit a recipe
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Recipe details
    path('recipes/', views.recipe_list, name='recipe_list'),  # Recipe list using CBV
    path('recipe/<int:id>/delete/', views.delete_recipe, name='delete_recipe'), # delete recipe
    path('my_recipes/', views.my_recipes, name='my_recipes'), #Page for user`s own recipes`
    path('login/', views.login_view, name='account_login'), #login page
    path('signup/', views.signup_view, name='account_signup'), #signup page
    path('logout/', views.logout_view, name='logout'), #logout page
    path('search/', views.search, name='search'),  # Search page
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #serve media files during development
