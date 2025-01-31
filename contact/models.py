from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class ContactForm(models.Model):
    """
    Stores a contact request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contacting request from {self.name}"

class ContactRequest(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request from {self.contact.name} on {self.request_date}"

