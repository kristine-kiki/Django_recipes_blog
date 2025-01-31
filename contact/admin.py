from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact, ContactRequest

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('message',)  

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    """
    Lists contact and request_date fields for display in admin
    """
    list_display = ('contact', 'request_date',)


