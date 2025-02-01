from django.contrib import admin
from .models import Category, Recipe
from django_summernote.admin import SummernoteModelAdmin


class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('ingredients', 'instructions')
    list_display = ('title', 'status', 'created_on', 'user')
    search_fields = ('title', 'ingredients', 'instructions')
    list_filter = ('status', 'created_on')
    ordering = ('-created_on',)
    readonly_fields = ('created_on',)
    fieldsets = (
        (None, {
            'fields': ('title', 'ingredients', 'instructions', 'cooking_time', 'categories', 'user', 'image', 'status')
        }),
    )

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)


