from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Recipe

# Create your views here.
def index(request):
    return HttpResponse("best recipe blog")