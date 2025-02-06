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
<li><strong>Users</strong><br> <strong>Fields:</strong> id, username, email, password, created_at<br> <strong>Description:</strong> Stores user information including their login credentials and registration timestamp.<br> <strong>Relationships:</strong><br>
One-to-Many: One user can submit multiple recipes.<br>
One-to-Many: One user can post multiple comments.<br>
One-to-Many: One user can rate multiple recipes.<br>
One-to-One: One user can have one admin role.<br>
One-to-Many: One user can submit multiple contact form entries.<br>
One-to-Many: One user can have multiple actions taken by admins. </li><br>
<li><strong>Recipes:</strong> <br> <strong>Fields:</strong> id, user_id, title, description, created_at, updated_at<br><strong>Description:</strong> Contains details of recipes submitted by users. user_id links to the user who submitted the recipe. updated_at tracks the last modification time.<br><strong>Relationships:</strong><br>
Many-to-One: Many recipes can be submitted by one user.
One-to-Many: One recipe can have multiple comments.<br>
One-to-Many: One recipe can have multiple ratings. </li><br>
<li><strong>Comments</strong><br> <strong>Fields:</strong> id, recipe_id, user_id, content, created_at, status, admin_id, approval_timestamp<br> <strong>Description:</strong> Holds comments made on recipes. status indicates whether a comment is pending, approved, or rejected. admin_id links to the admin who approved or rejected the comment, and approval_timestamp records the time of the action.<br> <strong>Relationships:</strong><br>
Many-to-One: Many comments can be made by one user.<br>
Many-to-One: Many comments can be made on one recipe.<br>
Many-to-One: Many comments can be approved or rejected by one admin.</li><br>
<li><strong>Ratings</strong><br> <strong>Fields:</strong> id, user_id, recipe_id, rating, comment, created_at<br> <strong>Description:</strong> Stores user ratings for recipes. rating is an integer between 1 and 5. Optionally, users can leave a comment along with their rating.<br> <strong>Relationships:</strong><br>
Many-to-One: Many ratings can be given by one user.<br>
Many-to-One: Many ratings can be given to one recipe. </li><br>
<li><strong>Admin Panel</strong><br> <strong>Fields:</strong> id, user_id, role, permissions, approval_status, created_at<br> <strong>Description:</strong> Manages admin roles and permissions. approval_status tracks the status of various actions (pending, approved, rejected).<br> <strong>Relationships:</strong><br>
One-to-One: One admin role can be assigned to one user.<br>
One-to-Many: One admin can approve or reject multiple comments.<br>
One-to-Many: One admin can handle multiple contact form entries.<br>
One-to-Many: One admin can perform multiple approvals or rejections. </li><br>
<li><strong>Approvals/Rejections</strong><br> <strong>Fields:</strong> id, admin_id, user_id, action, created_at<br> <strong>Description:</strong> Logs actions taken by admins regarding approvals and rejections and the created_at timestamp. <br> <strong>Relationships:</strong><br> Many-to-One: One admin can perform multiple approvals or rejections.<br>
Many-to-One: Many actions can be taken for one user.</li><br>
<li><strong>Contact Form</strong><br> <strong>Fields:</strong> id, user_id, admin_id, name, email, subject, message, created_at<br> <strong>Description:</strong> Stores information submitted through the contact form. Includes the user's ID, admin's ID handling the inquiry, user's name, email address, subject of the message, the message content, and the timestamp when the form was submitted.<br><strong>Relationships:</strong><br> 
Many-to-One: Many contact form entries can be handled by one admin.<br>
Many-to-One: Many contact form entries can be submitted by one user.</li><br>

## Testing
### Testing Using Validators
Upon completion of the writing process, developer used
[W3C MarkUp Validation Service](https://validator.w3.org/), <img src="readMe images\validator.w3.png"><br>
and [PEP8 online](http://pep8online.com/) to check the validity of the code. Code passed the tests with some errors that cannot be fixed. For example, too long lines that cannot be shortened or split in two.

Website was also tested using [Lighhouse](https://developers.google.com/web/tools/lighthouse). The following reports were generated on home and products pages:
<img src="readMe images/lighthouse.png">
<img src="readMe images/addrecipe.png">

### Manual Testing
The website was tested manually on both large and small screens during development. This included testing navigation, responsiveness across different screen sizes, database operations (Create, Read, Update, Delete), and overall application functionality.

### Client Stories Testing
The website was tested against the client stories to ensure all user requirements and expectations were met.

### Test Cases
Test Cases
Here's a list of some test cases performed for the recipe blog (just a part of them):

1.A user can register an account with a unique username - Pass;<br>
2.A user cannot register an account with a username that already exists in the database - Pass;<br>
3.Registered user can log in and log out - Pass;<br>
4.User can see a list of recipes - Pass;<br>
5.User can go to a recipe page and see its details, including comments and rating - Pass;<br>
6.Logged-in user can post comments and rate recipes - Pass;<br>
7.Comments appear after admin`s approval are associated with the correct recipe - Pass;<br>
8.Logged-in user can see own added recipes into My recipes - Pass;<br>
9.Logged-in user can see status of recipes - Pass;<br>
10.Logged-in user can edit and delete own recipes - Pass;<br>
11.Admin can approve or reject comments - Pass;<br>
12.Admin can add, update, and delete recipes through the website - Pass;<br>
13.Admin can manage user roles and permissions - Pass;<br>
14.All User can search for recipes using keywords - Pass;<br>
15.User can send a message using the contact form - Pass;<br>
16.Admin receives and can read contact form messages - Pass;<br>
17.All links are valid and redirect to the proper page - Pass.<br>

### Testing on Different Browsers and Devices
The website was tested and proved to be issue-free on the following browsers:
<li> Chrome</li>
<li> Edge</li>
<li> Firefox</li>
<li> Safari</li>

### Bugs and fixes
<li>Comments didn`t show up after Admin approved them. I add status field ('approved', 'pending', 'rejected').Updated logic in views and templates, to show just approved comments.
<li>The pop-up windows were not displaying correctly when the user wanted to delete a recipe. I added JavaScript to the base.html file to handle the pop-up functionality and used SweetAlert2 for better styling and UX
<li>Recipes were visible in the blog even when their status was pending and they hadn't been approved by the admin. I added a status field to track approval, updated the approval logic, and updated views and templates to show only approved recipes.</li>
<li>At the end of the project background image were not displayed correctly. i veryfied the correct path, ensured the image were in the correct directorie, and ran collectstatic command to gather static files.Cleared browsing data.</li>
<li>Many bugs were resolved using Django's debug mode. This feature made it easy to identify the causes of errors and address them. For more complex issues, I could quickly find solutions by searching for the exact error messages.</li>

## Cloning This Project
To create a clone, follow these steps:<br>
<li>Log in to GitHub and navigate to the repository.</li>
<li>Click on the "Code" button.</li>
<li>Select "Open with GitHub Desktop" and follow the prompts in the GitHub Desktop Application, or follow GitHub's instructions for cloning the repository using other methods.</li>

### Working with Your Local Clone
<li>Install the requirements from "requirements.txt" using pip install.</li>
<li>Build a new database with the commands python3 manage.py makemigrations and python3 manage.py migrate.</li>
<li>Create a new superuser by running python3 manage.py createsuperuser and follow the prompts.</li>
<li>Start the Django application using python3 manage.py runserver.</li>
<li>Log in using your superuser credentials by appending /admin to the URL.</li>
<li>From the admin panel, you can easily create, read, update, and delete records, including recipes, users, and email lists.</li>

## Deployment
The project was initially created in Gitpod and deployed on Heroku. Afterward, the project was migrated to VS Code for further development and maintenance.<br>
To deploy this application on Heroku, we are required to have a requirements.txt file as well as a Procfile. These files will allow Heroku understand what dependencies are required, as well as tell Heroku which file to run, in order to launch the web application.<br>
<li>Install production-ready webserver for Heroku</li>
    
    bash
    pip3 install gunicorn~=20.1
    
<li>Add to requirements file</li>
   
    bash
    pip freeze --local>requirements.txt
   
<li>Create a Procfile manually in the root directory. In Procfile write<br>
  
     web: gunicorn headchef.wsgi
this is the command Heroku will use to start the server<br>
<li>In settings.py file adjust ALLOWED_HOSTS by adding<br>
   
    ,'.herokuapp.com']

<li>Save and commit changes to GitHub.</li>
<li>Open Heroku and login or sign up.</li>
<li>Create a new app and select the desired region.</li>
<li>Connect Github to Heroku via the dashboard link "Deploy". Go to "Deployment method" and choose "GitHub", find your repository name listed and select it.</li>
<li>Once connected to GitHub repository, navigate to the "Settings" tab and reveal "Config Vars"</li>
<li>Create environment variables with your data (ensure names match those in settings.py):</li>
DATABASE_URL<br>
SECRET_KEY<br>
CLOUDINARY_API_KEY<br>
CLOUNINARY_API_SECRET<br>
CLOUDINARY_CLOUD_NAME<br>
<li>Disable "Automatic deploys" and deploy manually.</li>
<li>After couple minutes it should show "Your app was successfully deployed"</li>
<li>Open your newly created app</li>


## Learning Resources

- [How to create Django 404 and 500 page](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

## Credits
<li>BBC recipes (recipes and pictures has been copied)</li>
<li> The base.html file has been built on the foundation of the 'I think I can blog!' project
<li>SheCodes and Udemy
<li>Neverless my mentor Spencer Barriball
