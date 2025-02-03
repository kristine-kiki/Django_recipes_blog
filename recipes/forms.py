from django import forms
from .models import Recipe
from .models import Rating
from .models import Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'cooking_time', 'categories', 'user', 'image', 'status']
        exclude= ['user', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True  # Make the image field required
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)])
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']