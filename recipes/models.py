from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models import Avg

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=[('pending','Pending'),('approved','Approved'),('rejected','Rejected')],
        default='pending')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='edit')


    
    def average_rating(self) -> float:
        return Rating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"] or 0 

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]

class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.recipe.title}: {self.rating}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending',
        max_length=10
    )

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe}"