from django.contrib import admin
from .models import Category, Recipe
from django_summernote.admin import SummernoteModelAdmin


class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('ingredients', 'instructions')

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)


