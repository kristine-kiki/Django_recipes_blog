from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

# Create your views here.
def contact(request):
    
    if request.method == "POST":
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid():
                contact_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    'Contact request received!'
                )

    contact = Contact.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact,
         "contact_form": contact_form},
    )

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('success')  
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})