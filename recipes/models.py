from django.db import models  # impport Django models
from cloudinary.models import (
    CloudinaryField,
)  # import CloudinaryField for image storage
from django.contrib.auth.models import (
    User,
)  # import users model from Django`s auth system
from django.db.models import Avg  # import avg for calculating avarage ratings

# Create your models here.


class Category(models.Model):
    """
    model for recipe categories
    """

    name = models.CharField(
        max_length=75
    )  # category name with max lenght 75 characters

    def __str__(self):
        return self.name  # return category name


class Recipe(models.Model):
    """
    model for recipes
    """

    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Time in minutes")
    categories = models.ManyToManyField(
        Category
    )  # many-to-many relationship with categories
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField("image", null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="pending",
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, related_name="edit"
    )  # parent recipe for edited versions

    """
    method to calculate the avarege rating of the recipe
    """

    def average_rating(self) -> float:
        return (
            Rating.objects.filter(recipe=self).aggregate(Avg("rating"))["rating__avg"]
            or 0
        )

    """
    return recipe title
    """

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_on"]  # recipes order starting with latest added


class Rating(models.Model):
    """
    model for ratings given to recipe by a user
    """

    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="ratings"
    )  # recipe being rated
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # user who rated the recipe
    rating = models.IntegerField(default=0)  # given rating

    def __str__(self):
        return (
            f"{self.recipe.title}: {self.rating}"  # return the recipe title and rating
        )


class Comment(models.Model):
    """
    model for comments made by user on a recipe
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # user who made a comment
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )  # recipe comment was made to
    text = models.TextField()  # comment itself
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        default="pending",  # status of the comment
        max_length=10,
    )

    def __str__(self):
        return f"Comment by {self.user} on {self.recipe}"  # returns user and recipe
