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
<li><strong>User:</strong> Fields: id, username, email, password, created_at<br>
<strong>Description:</strong> Stores user information including their login credentials and registration timestamp.</li>
<li><strong>Recipes:</strong> Fields: id, user_id, title, description, created_at, updated_at <br>
<strong>Description:</strong> Contains details of recipes submitted by users. user_id links to the user who submitted the recipe. updated_at tracks the last modification time.</li>
<li><strong>Comments:</strong> Fields: id, recipe_id, user_id, content, created_at, status, admin_id, approval_timestamp<br>
<strong>Description:</strong> Holds comments made on recipes. status indicates whether a comment is pending, approved, or rejected. admin_id links to the admin who approved or rejected the comment, and approval_timestamp records the time of the action.</li>
<li><strong>Rating:</strong> Fields: id, user_id, recipe_id, rating, comment, created_at<br>
<strong>Description:</strong>Stores user ratings for recipes. rating is an integer between 1 and 5. Optionally, users can leave a comment along with their rating.</li>
<li><strong>Admin Panel</strong> Fields: id, user_id, role, permissions, approval_status, created_at <br>
<strong>Description:</strong> Manages admin roles and permissions. approval_status tracks the status of various actions (pending, approved, rejected).</li>
<li><strong>Approvals/Rejections</strong>Fields: id, admin_id, user_id, action, reason, created_at<br>
<strong>Description:</strong>Logs actions taken by admins regarding approvals and rejections. Includes the reason for the action and the created_at timestamp.

## Deployment
The project was initially created in Gitpod and deployed on Heroku. Afterward, the project was migrated to VS Code for further development and maintenance.

## Learning Resources

- [How to create Django 404 and 500 page](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

## Credits
<li>BBC recipes (recipes and pictures has been copied)</li>
<li> The base.html file has been built on the foundation of the 'I think I can blog!' project
<li>SheCodes and Udemy
