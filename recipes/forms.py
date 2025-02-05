from django import forms
from .models import Recipe
from .models import Rating
from .models import Comment

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe #Specifies this form is for Recipe model 
        fields = ['title', 'ingredients', 'instructions', 'cooking_time', 'categories', 'user', 'image', 'status']
        exclude= ['user', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = True  # Make the image field required

# RatingForm class is used to handle form data for creating and updating Rating instances       
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating #Specifies this form is for Rating model
        fields = ['rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, i) for i in range(1, 6)]) #use radio buttonss for rating recipes, choices (1-5)
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #Specifies this form is for Comment model
        fields = ['text'] #includes only the text field in the form