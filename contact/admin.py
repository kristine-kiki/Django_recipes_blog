from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ContactForm

@admin.register(ContactForm)
class ContactAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('message',)  




