from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    """
    Handles contact form submissions and displays success message.
    """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your message has been sent successfully!")
            form = ContactForm()
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'contact_form': form})
