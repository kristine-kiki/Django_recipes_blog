# Recipes Blog 

[Recipe Blog](https://django-recipes-blog-489bc206e230.herokuapp.com/)<br>
<img src="readMe images\home page.png">

## Introduction

Welcome to the [Recipe Blog](https://django-recipes-blog-489bc206e230.herokuapp.com/) repository! This project is crafted for cooking enthusiasts to connect, share, and celebrate the joy of cooking and delicious recipes. Dive in to explore, add your own recipes, comment on others, and rate your favorites. Admin ensures that the content remains clean and adheres to the community guidelines.

## Getting Started


### Installation

1. **Install Jango**

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

<li>JavaScript: Enhances interactive features.</li>

<li>HTML/CSS: Structures and styles the web pages.
</li>

## Features
<li>User Registration and Authentication: Built using Django's built-in authentication system. Allows users sign up, log in and manage their profile/recipes.</li>

<li>Recipe Management: Users can add, edit, and delete their own culinary creations. Six latest recipes are displayed on Home page with a modal pop-up showing detailed information. Other recipes are stored in All Recipes section. Admin approves recipes and pictures to maintain quality.</li>

<li>Search Functionality: Easily find recipes or ingredients using search tool.</li>

<li>Comments and Ratings: Engage with the community by leaving comments and ratings on recipes. Admin approve comments to maintain quality.</li>

<li>Responsive Design: The application is built using Bootstrap for a responsive and user-friendly design and ensures a seamless experience across various devices.</li>

<li>Admin Panel: Efficiently manage users, recipes, comments and pictures through the Django Admin panel.</li>

## Project Structure
<li>`headchef/` - Main project directory containing settings and configuration files.</li>
<li>`recipes/` - Primary app directory containing the main blog application.</li>
<li>`contact/` - Secondary app directory for the contact form and user inquiries.</li>

## Learning Resources

- [How to create Django 404 and 500 page](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

### How to make a ERD diagram 
<img src="readMe images\diagram.png">
