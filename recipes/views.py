from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.views.generic import ListView, DetailView
from .models import Recipe, Rating, Comment
from .forms import RecipeForm, RatingForm, CommentForm

# Create your views here.


# home view to display the latest 6 approved recipes.
def home(request):
    """
    Display latest 6 approved recipes with average ratings and
    approved comments.  Models: Recipe and Comment
    """
    recipes = Recipe.objects.filter(status="approved").order_by("-created_on")[:6]
    for recipe in recipes:
        recipe.average_rating = recipe.ratings.aggregate(Avg("rating"))[
            "rating__avg"
        ]  # display avarage rating
        recipe.approved_comments = Comment.objects.filter(
            recipe=recipe, status="approved"
        )  # Filter approved comments
    return render(
        request,
        "home.html",
        {
            "recipes": recipes,
        },
    )


# Class-based view to list recipes with pagination. Model:Recipe
class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipe_list.html"
    context_object_name = "recipes"
    paginate_by = 6


# Function-based view to list recipes with pagination.
def recipe_list(request):
    """
    Fetch approved recipes and original recipes awaiting editing approval
    Model:Recipe
    """
    recipes = Recipe.objects.filter(status="approved")
    for recipe in recipes:
        print(recipe.image.url)
    paginator = Paginator(recipes, 6)  # Paginate by 6 recipes per page
    page_number = request.GET.get("page")  # Get the current page number
    page_obj = paginator.get_page(page_number)  # Paginate the query

    return render(
        request,
        "recipes/recipe_list.html",
        {
            "page_obj": page_obj,  # Pass the paginated recipes to the template
        },
    )


# view to add a new recipe.
@login_required(login_url="account_login")
def add_recipe(request):
    """
    Handle submission of a new recipe and display the form.
    Model:Recipe
    """
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.status = "pending"
            recipe.save()
            form.save_m2m()
            messages.add_message(
                request, messages.SUCCESS, "Recipe submitted for approval!"
            )
            return redirect("recipe_list")
    else:
        form = RecipeForm()

    return render(request, "recipes/add_recipe.html", {"form": form})


# view to edit an existing recipe.
@login_required
def recipe_edit(request, recipe_id):
    """
    Handle editing of an existing recipe and display the form.
    Model:Recipe
    """
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.user != request.user:
        messages.error(request, "Not authorized to edit this recipe.")
        return redirect("recipe_detail", recipe_id=recipe_id)
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe_edited = form.save(commit=False)
            recipe_edited.status = "pending"
            recipe_edited.parent = (
                recipe  # Link the edited version to the original recipe
            )
            recipe_edited.save()
            form.save_m2m()
            messages.add_message(
                request, messages.SUCCESS, "Edition submitted for approval"
            )
            return redirect("my_recipes")
    else:
        form = RecipeForm(instance=recipe)

    return render(
        request,
        "recipes/recipe_edit.html",
        {
            "form": form, "recipe": recipe
        }
    )


# view to delete recipe.
def delete_recipe(request, id):
    """
    Handle deletion of recipe.
    Model:Recipe
    """
    # Get the recipe object or return a 404 error if not found
    recipe = get_object_or_404(Recipe, id=id)

    # Check if the current user is the owner of the recipe
    if recipe.user != request.user:
        messages.error(request, "Not authorized to delete this recipe.")
        return redirect("recipe_detail", recipe_id=id)

    # Delete the recipe
    recipe.delete()

    # Display a success message
    messages.success(request, "Recipe deleted successfully.")

    # Redirect to the list of recipes/ All recipes
    return redirect("recipe_list")


# view to display user`s own recipes
@login_required
def my_recipes(request):
    """
    Display recipes submitted by the logged-in user.
    Model:Recipe
    """
    recipes = Recipe.objects.filter(user=request.user)
    return render(
        request,
        "recipes/my_recipes.html",
        {
            "recipes": recipes,
        },
    )


# class-based view to display the details of recipe.Model:Recipe
class RecipeDetail(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"


# view to search for recipes.
def search(request):
    """
    Search queries for recipes and display results.
    Model:Recipe
    """
    query = request.GET.get("query")
    if query:
        results = Recipe.objects.filter(title__icontains=query) | Recipe.objects.filter(
            ingredients__icontains=query
        )
    else:
        results = Recipe.objects.none()
    return render(request, "recipes/search_results.html", {"results": results})


# view to display details of a recipe and handle rating and comment submissions.
def recipe_detail(request, recipe_id):
    """
    Display details of a recipe, ratings and comments.
    Handle rating and comment submissions.
    Models: Recipe, Comment, Rating
    """
    recipe = get_object_or_404(Recipe, id=recipe_id, status__in=["approved", "pending"])
    comments = Comment.objects.filter(
        recipe=recipe, status="approved"
    )  # Show only approved comments
    ratings = recipe.ratings.all()
    user_rating = (
        ratings.filter(user=request.user).first()
        if request.user.is_authenticated
        else None
    )

    # Initialize forms
    rating_form = RatingForm()  # form to handle rating submissions
    comment_form = CommentForm()  # Initialize the comment form
    rating_range = [1, 2, 3, 4, 5]  # A range of rating options (1 to 5)

    # Handle POST requests (rating and comment submission)
    if request.method == "POST":
        if "rating_submit" in request.POST:  # Handle rating submission
            rating_value = request.POST.get("rating")
            if rating_value:
                # Save the rating to the database
                rating_value = int(rating_value)
                user_rating, created = Rating.objects.update_or_create(
                    user=request.user, recipe=recipe, defaults={"rating": rating_value}
                )

                if created:
                    messages.success(request, "Your rating has been submitted!")
                else:
                    messages.info(request, "Your rating has been updated!")
                return redirect("recipe_detail", recipe_id=recipe_id)

        elif "comment_submit" in request.POST:  # Handle comment submission
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.recipe = recipe
                comment.status = "pending"
                comment.save()
                messages.success(request, "Your comment waiting for approval!")
                return redirect("recipe_detail", recipe_id=recipe_id)

    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "ratings": ratings,
            "user_rating": user_rating,
            "rating_form": rating_form,
            "comment_form": comment_form,
            "rating_range": rating_range,
        },
    )


# view to handle user login
def login_view(request):
    """
    Handle user login and display login form
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


# view to handle user signup
def signup_view(request):
    """
    Handle user sign up and display the signup form
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account_login")  # Redirect to the login page
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


# view to handle user logout
def logout_view(request):
    """
    Handle user logout
    """
    if request.method == "POST":
        logout(request)
        return redirect("home")  # Redirect to the homepage after logout
    return render(request, "registration/logout.html")
