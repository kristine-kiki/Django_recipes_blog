from django.contrib import admin
from .models import Category, Recipe, Comment
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

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'recipe', 'status', 'created_at')  # Display relevant fields
    list_filter = ('status',)  # Allow filtering by status (pending, approved, rejected)
    search_fields = ('user__username', 'recipe__title', 'text')  # Enable search by username, recipe title, and comment text
    actions = ['approve_comments', 'reject_comments']  # Bulk actions for admin

    def get_user(self, obj):
        return obj.user.username  # Show the username in the admin panel
    get_user.admin_order_field = 'user'
    get_user.short_description = 'User'

    def approve_comments(self, request, queryset):
        queryset.update(status='approved')  # Bulk approve comments
    approve_comments.short_description = "Approve selected comments"

    def reject_comments(self, request, queryset):
        queryset.update(status='rejected')  # Bulk reject comments
    reject_comments.short_description = "Reject selected comments"

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)


