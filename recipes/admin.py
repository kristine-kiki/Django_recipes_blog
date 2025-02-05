from django.contrib import admin #import Django`s admin module
from .models import Category, Recipe, Comment #models from the current app
from django_summernote.admin import SummernoteModelAdmin #SummernoteModelAdmin for rich text editing
from django.utils.html import mark_safe #mark-safe to safely render HTML

# admin class for Recipe model
class RecipeAdmin(SummernoteModelAdmin):
    summernote_fields = ('ingredients', 'instructions') #use Summernote for ingredients and instructions fields
    list_display = ('title', 'status', 'created_on', 'user', 'image_tag')  # includes image_tag in list display
    search_fields = ('title', 'ingredients', 'instructions') # enable search by title, ingredients and instructions
    list_filter = ('status', 'created_on') #enable filtering by status and creation date
    ordering = ('-created_on',) #order by creation date
    readonly_fields = ('created_on', 'image_tag')  # Make image_tag readonly to display it
    fieldsets = (
        (None, {
            'fields': ('title', 'ingredients', 'instructions', 'cooking_time', 'categories', 'user', 'image', 'status')
        }),
    )
    # custom method to display the image in the admin
    def image_tag(self, obj): 
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')  # display thumbnail image
        return 'No image'
    image_tag.short_description = 'Image'

# admin class for comment model
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'recipe', 'status', 'created_at')  # display relevant fields
    list_filter = ('status',)  # allow filtering by status (pending, approved, rejected)
    search_fields = ('user__username', 'recipe__title', 'text')  # enable search by username, recipe title, and comment text
    actions = ['approve_comments', 'reject_comments']  # bulk actions for admin
    
    #custom method to get the username
    def get_user(self, obj):
        return obj.user.username  # show the username in the admin panel
    get_user.admin_order_field = 'user' #order for users
    get_user.short_description = 'User' #short description

    #action to approve selected comments
    def approve_comments(self, request, queryset):
        queryset.update(status='approved')  # Bulk approve comments
    approve_comments.short_description = "Approve selected comments"

    #action to reject selected comments
    def reject_comments(self, request, queryset):
        queryset.update(status='rejected')  # Bulk reject comments
    reject_comments.short_description = "Reject selected comments"

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment, CommentAdmin)


