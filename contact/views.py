from django.shortcuts import render, redirect
from django.contrib import messages #import messages for displaying messages to the user
from .models import ContactForm #import ContactForm model
from .forms import ContactMessageForm #import ContactMessageForm from forms


def contact_view(request):
    """
    Handles contact form submissions and displays success message.
    """
    if request.method == "POST":
        form = ContactMessageForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:        
        form = ContactMessageForm()

    return render(request, 'contact/contact.html', {'contact_form': form })


