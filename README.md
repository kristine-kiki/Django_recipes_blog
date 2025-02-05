# Recipes Blog 

[Recipe Blog](https://django-recipes-blog-489bc206e230.herokuapp.com/)<br>
<img src="readMe images\Screenshot 2025-02-05 at 20.39.22.png">

## Introduction

Welcome to the [Recipe Blog](https://django-recipes-blog-489bc206e230.herokuapp.com/) repository! This project is crafted for cooking enthusiasts to connect, share, and celebrate the joy of cooking and delicious recipes. Dive in to explore, add your own recipes, comment on others, and rate your favorites. Admin ensures that the content remains clean and adheres to the community guidelines.<br>Users can view their added recipes in the "My Recipes" section, where the status of each recipe—whether approved or still pending—is displayed. Additionally, Admin have the authority to change recipe pictures if necessary to ensure that the images accurately reflect the dishes described in the recipes.<br>If users want to reach out to the Recipe Blog's admin, they can easily send a message through the contact form available on the site. This allows for efficient communication and prompt responses to user inquiries.

## Features
<li><strong>User Registration and Authentication:</strong> Built using Django's built-in authentication system. Allows users sign up, log in and manage their profile/recipes.</li>

<li><strong>Recipe Management:</strong> Users can add, edit, and delete their own culinary creations. Six latest recipes are displayed on Home page with a modal pop-up showing detailed information. Other recipes are stored in All Recipes section. Admin approves recipes and pictures to maintain quality.</li>

<li><strong>Search Functionality:</strong> Easily find recipes or ingredients using search tool.</li>

<li><strong>Comments and Ratings:</strong> Engage with the community by leaving comments and ratings on recipes. Admin approve comments to maintain quality.</li>

<li><strong>Responsive Design:</strong> The application is built using Bootstrap for a responsive and user-friendly design and ensures a seamless experience across various devices.</li>

<li><strong>Admin Panel:</strong> Efficiently manage users, recipes, comments and pictures through the Django Admin panel.</li>

### User stories
As a/an .. | I want to be able to ..
--------|------------------------
User | easily understand the main purpose of the blog 
User | easily navigate throughout the blog to find content.
User | in Home page see the latest 6 recipes.
User | see a list of all recipes.
User | see each recipe in more detail.
User | see comments and ratings for each recipe.
User | send the contact form to admin.
User | sign up for the blog.
Authorized User | sign in and logout of the blog.
Authorized User | add recipes what are displayed in All recipes and My recipes.
Authorized User | add coments and ratings to recipes.
Authorized User | edit my recipes and change rating for recipes.
Authorized User | see the status of recipes I created in My recipes
Authorized User | delete recipes I created
Admin | approve, reject new Users.
Admin | add new, edit or delete recipe categories.
Admin | add new, edit or delete recipes
Admin | add new, edit or delete pictures for recipes.
Admin | add new, edit or delete comments
Admin | receive and read Contact form. 

## Getting Started


### Installation

1. **Install Django**

    ```bash
    pip3 install Django~=4.2.1
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Create project**
    ```bash
    django-admin startproject headchef .
    ```
4. **Start app**
    ```bash
    python3 manage.py startapp recipes
    ```

### Running the Project
1. **Create superuser**
    ```bash
    python3 manage.py createsuperuser
    ```

2. **Create Models and apply Migrations**
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

3. **Run the Server**
    ```bash
    python3 manage.py runserver
    ```
    Open your browser and go to `http://127.0.0.1:8000` to see my Recipe Blog project in action.

## Programs Used
<li>Django: Backend framework.</li>
<li>Bootstrap: For responsive and sleek design.</li>
<li>PostgreSQL: Database for storing user data, recipes, and comments.</li>
<li>GitHub: Version control</li>
<li>PIP: Python package manager for installing dependencies</li>
<li>Heroku: Cloud platform for deployment</li>
<li>Favicon: Tool to generate favicons</li>
<li>SweetAlert2: Customizable alerts for better user experience</li>
<li>JavaScript: Enhances interactive features.</li>
<li>HTML/CSS: Structures and styles the web pages.
</li>

## Project Structure
<li>`headchef/` - Main project directory containing settings and configuration files.</li>
<li>`recipes/` - Primary app directory containing the main blog application.</li>
<li>`contact/` - Secondary app directory for the contact form and user inquiries.</li>

## ERD diagram 
<img src="readMe images\diagramma.png"><br>
<li>User: One-to-Many with Recipes (a user can create multiple recipes)<br>
One-to-Many with Comments (a user can leave multiple comments)<br>
One-to-Many with submiting contact forms (a user can submit multiple contact forms)</li>
<li>Recipe: Many-to-One with User (a recipe can be created by one user)<br>
One-to-Many with Comments (a recipe can have multiple comments)<br>
One-to-Many with Ratings (a recipe can have multiple ratings).</li>
<li>Comment: Many-to-One with User (A comment is left by one user)<br>
Many-to-One with Recipe (A comment belongs to one recipe) Needs Admin`s approval.</li>
<li>Rating: Many-to-one with user (A rating is given by one user) <br>Many-to-One with Recipe (A rating belongs to one recipe)</li>
<li>ContactFormSubmission: Many-to-One with User (a contact form submission can be submitted by one user).</li>

## Deployment
The project was initially created in Gitpod and deployed on Heroku. Afterward, the project was migrated to VS Code for further development and maintenance.

## Learning Resources

- [How to create Django 404 and 500 page](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

## Credits
<li>BBC recipes (recipes and pictures has been copied)</li>
<li> The base.html file has been built on the foundation of the 'I think I can blog!' project
<li>SheCodes and Udemy
