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

## Agile Development Approach

This project was developed following Agile principles to allow for iterative development, flexibility, and continuous improvement. While primarily a solo project, the Agile mindset was applied through:

*   **User Stories:** The project began by defining clear user stories to capture the core requirements from different user perspectives. These served as the backlog of features to be implemented.
*   **Iterative Development:** Features were developed in manageable chunks or iterations. For example, user authentication might be one iteration, followed by recipe creation, then commenting, etc. This allowed for focusing on specific functionalities and testing them before moving to the next.
*   **Prioritization:** User stories and tasks were implicitly prioritized based on core functionality needed for a minimum viable product (MVP) and then expanded upon.
*   **Regular Review (Self-Review):** At the end of developing a feature or a set of related features, a self-review process was undertaken to check against the user stories, test functionality, and identify any immediate bugs or areas for improvement.
*   **Adaptability:** The Agile approach allowed for adapting to challenges or new insights during development. For instance, if a particular implementation proved difficult, alternative approaches could be considered. The "Bugs and Fixes" section reflects some of the adaptations and problem-solving that occurred.

While formal Agile ceremonies were not applicable to this solo project, the core values of delivering working software incrementally, responding to feedback (even self-generated or from mentors), and focusing on user needs were central to the development process. The User Stories section and the "Bugs and Fixes" section provide insight into this iterative approach.

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

## Design Process & UX/UI

A thoughtful design process was undertaken to ensure the Recipe Blog is intuitive, user-friendly, and visually appealing, aligning with the goal of creating a welcoming space for cooking enthusiasts.

### Design Philosophy
The core design philosophy was to create a clean, organized, and accessible interface. Key considerations included:
*   **Clarity:** Ensuring that users can easily find recipes, understand site navigation, and interact with features like commenting and rating.
*   **Simplicity:** Avoiding clutter and unnecessary complexity to keep the focus on the recipes and community interaction.
*   **Responsiveness:** Prioritizing a seamless experience across all devices, from desktops to mobile phones, achieved through the use of Bootstrap.
*   **Engagement:** Encouraging user participation through clear calls to action for adding recipes, commenting, and rating.

The initial inspiration was drawn from popular recipe platforms, focusing on elements that contribute to a positive user experience, such as clear recipe layouts and intuitive search functionality.

### Background Imagery
A key element of the visual design is the use of high-quality, food-themed background imagery.
*   **Style:** The primary background image is a photographic flat-lay or still life composition featuring fresh culinary ingredients such as carrots, onions, cabbage, a bottle of oil, and other kitchen staples.
*   **Placement:** This image is prominently used as a full-width banner at the top of pages and also appears as a subtle, textured backdrop behind the main content area on pages like "All Recipes".
*   **Purpose:** The imagery serves to immediately establish the blog's theme, create an inviting and appetizing atmosphere, and visually engage the user, reinforcing the focus on cooking and fresh ingredients.
![Main Background Image Snippet](/readMe%20images/blogbackground.jpg)


### Wireframes
To visualize the structure and layout of key pages before development, a series of wireframes were created. These helped in planning the placement of elements and user flow.

**1. Main Pages (Recipe List & Add Recipe Form):**
   The image below shows the wireframes for the main recipe listing page and the "Add Recipe" form page.
   ![Wireframes for Main Recipe List and Add Recipe Form](/readMe%20images/wireframe.png) 
   
   *   **Main Recipe List Page (Left in image):** Includes header navigation, a prominent search bar, a grid display for recipe cards (each with an image, title, rating, and view button), and a footer.
   *   **Add Recipe Form Page (Right in image):** Includes a header, a structured form with fields for title, ingredients, instructions, cooking time, categories, image upload, and a submission button, along with a footer.

**2. User Interaction Pages (Contact & My Recipes):**
   Further wireframes were developed for key user interaction pages, as shown below.
   ![Wireframes for Contact Us and My Recipes Pages](/readMe%20images/wireframe1.png) 
   *   **Contact Us Page (Left in image):** Features a title, introductory text, input fields for Name, Email, and Message, and a submit button, all within a standard header/footer layout.
   *   **My Recipes Page (Right in image):** Designed to display a list of recipes submitted by the logged-in user. It includes a title, an "Add Recipe" button, and a list view where each recipe displays its title and current status (e.g., approved/pending).

### Colour Scheme & Palette
The color scheme was chosen to be inviting, to complement food imagery, and to ensure good readability and visual hierarchy. The defined palette below was used consistently throughout the application. If CSS custom properties were used, their names are listed below.
![Colour Scheme](/readMe%20images/hexcode.png)

### Typography
The fonts were selected for readability and to match the overall aesthetic of the blog.
*   **Headings:** Font Name, Roboto - Chosen for its clean and modern look, providing clear visual hierarchy.
*   **Body Text:** Font Name, also Roboto - Selected for its excellent readability across different screen sizes.


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

## Technology Rationale

The technologies for this project were chosen to provide a robust, scalable, and maintainable platform for the Recipe Blog, and to leverage their strengths for specific project needs:

*   **Python & Django:** Python was selected for its readability and extensive libraries. Django, as a high-level Python web framework, was chosen for its "batteries-included" philosophy, providing a powerful ORM for database interaction, a built-in administrative panel for easy content management, security features, and a structured approach (MVT - Model-View-Template) that accelerates web development.
*   **PostgreSQL:** Utilized as the relational database in production (Heroku) for its reliability, data integrity, and advanced features suitable for scalable applications. (During local development, Django's default SQLite may have been used for simplicity).
*   **HTML, CSS, JavaScript:** These are the foundational web technologies. HTML structures the content, CSS (with Bootstrap) styles it, and JavaScript enhances user interactivity, particularly with features like SweetAlert2.
*   **Bootstrap:** Integrated for frontend styling to ensure a responsive, mobile-first design. Its grid system and pre-styled components allowed for rapid development of a consistent and user-friendly interface across various devices.
*   **Cloudinary:** Chosen for external image management. This offloads image storage and processing (like resizing or format conversion) from the main application server, improving performance and simplifying image handling.
*   **Heroku:** Selected as the Platform-as-a-Service (PaaS) for deployment, due to its ease of use for Django applications, integration with GitHub, and management of server infrastructure.
*   **SweetAlert2:** Implemented to provide richer, more engaging user notifications and confirmation dialogs (e.g., for recipe deletion) compared to standard browser alerts, enhancing the overall user experience.
*   **Git & GitHub:** Utilized for version control, enabling systematic tracking of code changes, collaboration (if applicable), and providing a history of the project's development.
*   **Gunicorn:** Used as the WSGI HTTP server for running the Django application in the Heroku production environment, as it's a common and robust choice for Python web applications.

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

### Manual Testing and Test Cases

The website was tested manually on both large and small screens during development. This included testing navigation, responsiveness across different screen sizes, database operations (Create, Read, Update, Delete), and overall application functionality. The website was also tested against the client stories to ensure all user requirements and expectations were met.
Below is a sample of the detailed test cases performed:

| Test ID | Feature / User Story ID | Test Description                                       | Steps to Reproduce                                                                                                | Expected Result                                                                                                | Actual Result | Pass/Fail |
|---------|-------------------------|--------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|---------------|-----------|
| TC-001  | US-Signup               | A user can register an account with a unique username. | 1. Navigate to the "Register" page. <br>2. Enter a unique username, email, and password. <br>3. Click "Sign Up".         | User account is created. User is redirected to the login page. A success message for registration is displayed.    | As expected   | Pass      |
| TC-002  | US-Signup               | A user cannot register with an existing username.      | 1. Navigate to the "Register" page. <br>2. Enter an already existing username, email, and password. <br>3. Click "Sign Up". | An error message is displayed indicating the username is already taken. User remains on the registration page.     | As expected   | Pass      |
| TC-003  | US-LoginLogout          | A registered user can log in and log out.              | 1. Navigate to "Login" page. <br>2. Enter valid credentials. Click "Login". <br>3. Click "Logout" link.                  | User successfully logs in. After clicking logout, user is logged out and redirected (e.g., to home page).         | As expected   | Pass      |
| TC-004  | US-ViewRecipes          | A user can see a list of all approved recipes.         | 1. Navigate to the "All Recipes" page.                                                                            | A list/grid of approved recipes is displayed, showing titles, images, and brief descriptions.                  | As expected   | Pass      |
| TC-005  | US-ViewRecipes          | A user can view recipe details, comments, and rating.  | 1. From "All Recipes", click on a recipe's "View Recipe" button.                                                  | The full recipe details page is displayed, including ingredients, instructions, comments, and average rating.      | As expected   | Pass      |
| TC-006  | US-AddCommentRating     | A logged-in user can post comments and rate recipes.   | 1. Log in. <br>2. Navigate to a recipe detail page. <br>3. Submit a comment and a rating using the respective forms.  | Comment is submitted (pending approval). Rating is submitted/updated. Appropriate success messages are shown.   | As expected   | Pass      |
| TC-007  | US-AdminComments        | Approved comments are displayed on the recipe page.    | 1. As Admin, approve a pending comment. <br>2. As a User, navigate to the recipe detail page for that recipe.     | The newly approved comment is visible under the recipe.                                                        | As expected   | Pass      |
| TC-008  | US-ViewMyRecipes        | A logged-in user can see their own added recipes.      | 1. Log in. <br>2. Navigate to the "My Recipes" page.                                                              | A list of recipes created by the logged-in user is displayed.                                                  | As expected   | Pass      |
| TC-009  | US-ViewMyRecipes        | A logged-in user can see the status of their recipes.  | 1. Log in. <br>2. Navigate to "My Recipes".                                                                       | Each recipe in the list displays its current status (e.g., "Pending", "Approved").                             | As expected   | Pass      |
| TC-010  | US-EditRecipeRating / US-DeleteRecipe | A logged-in user can edit and delete their own recipes. | 1. Log in. <br>2. Go to "My Recipes". <br>3. Click "Edit" on a recipe, modify, and save. <br>4. Click "Delete" on a recipe and confirm. | Recipe is successfully updated after editing. Recipe is successfully removed after deletion.                  | As expected   | Pass      |
| TC-011  | US-AdminComments        | An admin can approve or reject comments.               | 1. Log in as Admin. <br>2. Navigate to the admin panel section for comments. <br>3. Approve a pending comment. <br>4. Reject another pending comment. | Comment status changes to "Approved" or is removed/marked as "Rejected".                                     | As expected   | Pass      |
| TC-012  | US-AdminRecipes         | An admin can add, update, and delete recipes.          | 1. Log in as Admin. <br>2. Use admin interface to add a new recipe. <br>3. Edit an existing recipe. <br>4. Delete a recipe. | Admin can perform all CRUD operations on recipes successfully.                                                 | As expected   | Pass      |
| TC-013  | US-AdminUsers           | An admin can manage user roles and permissions.        | 1. Log in as Admin. <br>2. Navigate to the user management section in admin panel. <br>3. Modify a user's status or permissions (e.g., make staff). | User permissions/roles are updated as per admin actions.                                                       | As expected   | Pass      |
| TC-014  | US-Search               | Any user can search for recipes using keywords.        | 1. On any page with search bar, enter a keyword (e.g., "chicken", "pasta"). <br>2. Click "Search".                   | A list of recipes matching the keyword in title or ingredients is displayed.                                   | As expected   | Pass      |
| TC-015  | US-Contact              | A user can send a message using the contact form.      | 1. Navigate to the "Contact" page. <br>2. Fill in name, email, and message. <br>3. Click "Submit".                  | A success message is displayed, and the message is sent to the admin system.                                   | As expected   | Pass      |
| TC-016  | US-Contact              | An admin receives and can read contact form messages.  | 1. Log in as Admin. <br>2. Navigate to the admin section for contact messages.                                    | Submitted contact messages are visible and readable by the admin.                                              | As expected   | Pass      |
| TC-017  | US-Navigation           | All links are valid and redirect to the proper page.   | 1. Click on all navigation links in header/footer. <br>2. Click on various internal links (e.g., "View Recipe"). | All links navigate to the correct and intended pages without errors (e.g., 404s).                              | As expected   | Pass      |

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
<li>Categories were not being correctly saved or "pulled in" when creating or editing recipes.
Fix: Identified missing form.save_m2m() calls after form.save(commit=False) in add_recipe and recipe_edit views. Added this line to both views, resolving the issue.</li>

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

## Future Enhancements
*   **Advanced Search Filters:** Allow users to filter recipes by category, cooking time, or user ratings.
*   **User Profile Pages:** More detailed user profiles where users can showcase their submitted recipes, favorite recipes, and perhaps a short bio.
*   **Social Sharing:** Integration to allow users to easily share recipes on social media platforms.
*   **Nutritional Information:** Option for users to add approximate nutritional information for their recipes.
*   **Image Galleries for Recipes:** Allow users to upload multiple images per recipe.
*   **Print-Friendly Recipe View:** A dedicated view for recipes optimized for printing.

## Learning Resources

- [How to create Django 404 and 500 page](https://learndjango.com/tutorials/customizing-django-404-and-500-error-pages)

## Credits
<li>BBC recipes (recipes and pictures has been copied)</li>
<li> The base.html file has been built on the foundation of the 'I think I can blog!' project
<li>SheCodes and Udemy
<li>Neverless my mentor Spencer Barriball
