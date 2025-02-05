from django import forms
from .models import ContactForm

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('name', 'email', 'message')