"""
URL configuration for headchef project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin #import admin module to enable the admin interface
from django.urls import path, include #import path and anclude functions to define URL patterns
from recipes import views #impot views from the recipe app
from django.contrib.auth import views as auth_views #import auth views for autification
from django.conf.urls.static import static #import statics to serve static and media files during development
from django.conf import settings #import settings to access project settings

urlpatterns = [
    path('accounts/', include("allauth.urls")), #include allauth URLs for user autheficiation and account managment
    path('admin/', admin.site.urls), #URL pattern for the admin interface
    path('summernote/', include('django_summernote.urls')), #include summernote URLs for rich text editing
    path('contact/', include('contact.urls'), name='contact'), #include contact app URLs
    path('login/', auth_views.LoginView.as_view(), name='login'), #URL pattern for the login view
    path('', include('recipes.urls'), name="home"), #URLs from the recipes app with the home Url pattern
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #serve media files during development
