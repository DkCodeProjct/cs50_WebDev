
##### Overview.
    - I've needed a blog for myself, so I'm glad I've made one. Also, I believe I've completed all the CS50 requirements for the final project. I used JavaScript and Bootstrap together to ensure that this application is mobile-responsive, and all functionalities work as expected..
    
    NOTE: also i dont thik i need requarment.txt file because ive only use django built in functonalities and js boostrap.
    
    - youtTube Project Video Link:
        * Link:[  https://youtu.be/zm4YUjtoU-U  ]
    
## Distinctiveness and Complexity.

    + I've created a blog website where users can post their blog entries. This project uses a tow models, which I believe is sufficient as it presents the necessary information effectively, ensuring a minimalist user experience. 
    
    + I've utilized JavaScript and Bootstrap to enhance the webpage's user-friendliness and, most importantly, to make it mobile-responsive.

    + i belive my js function for go back to the top of page[goUp] is sufficiently distinct from the other projects in this course

    + also this project was built using Django with 2 models on the back-end and JavaScript, Boostrap in the front-end for updating and displaying content also making user experience interactive.

    + and cs50 Required  this project is also mobile responsive. Each page sizes its elements to fit the width of a mobile devices. 


## Models.

- model User[Abstractuser].
    * The User model extends Django's built-in AbstractUser, adding custom relationships for user groups and permissions with specific related names to avoid conflicts.

- model BlogPost.
    *  this model represents individual blog post Detail/Data, linking each post to a user (author) via a foreign key relationship. It includes fields for an image URL (imgUrl), title, content (post), and the date of creation (date). This setup allows users to create and manage their blog posts, with each post associated with its respective author.

## View Functions in this Project.

- Login, Logout, Register.
    A.  these func helps to give user Features like Delete,Add If user Login, Else they show Existing Posts
    
    B. if user input Wrong password or Gmail the func render Error massages and prevent user from login.
    else the user will sign in  and will have ability to use all the features in blog website

-  confirmDel, deletePost.
    A. function displays a confirmation page to verify that the logged-in user wants to delete a specific blog post. The deletePost function actually deletes the post if the user confirms the deletion via a POST request. Both functions ensure that only the post's author can perform these actions.

    
- create_blog_post.
    A. Allows logged-in users to create new blog posts. It handles both the display of the form to create a post and the processing of form submission to save the post to the database.

- postContent, index.
    A. These two functions together manage the display of blog content in the web application. The "index" function showcases a list of all blog posts, arranging them by date, thus enabling users to peruse the latest entries conveniently.
    B. Meanwhile, the "post_content" function facilitates the presentation of a specific blog post, accessed through its unique identifier. This function retrieves the chosen post from the database and exhibits its full content on a dedicated page for users to engage with.


## Js Funcs.

- goUp.
    A. This JavaScript code snippet enhances user experience by implementing a "go up" button functionality on a webpage. The onscroll event listener triggers the display of a button (goUp) when the user scrolls down to a certain point on the page. 
    
    B. When clicked, the goUp() function smoothly scrolls the page back to the top. This feature improves navigation, allowing users to easily return to the top of the page without manually scrolling.

## Templates.
- index, content .html Pages.
    A. These pages are about Showing Posts and post Content

- delete.html.
    A. give user ability to Delete Post and ask user to confirm me the deletion
- login, register .html pages.
    A. these html pages a resposible for login,logout  and register operations.

- userPost.html.
    A. show User Posts, more behave like a user Profile
- post.html
    A. Where you can create Post

## files in this project.

-admin.py: registers Django models to be used in the application.

-models.py: contains the Models or tables that are to be used with the SQLite database.

-urls.py: contains the application's urls.

-views.py: contains all the view functions of the application.

- static/style.css: contain css for the html pages


#### How to run this application:
    A.Install Python if not already done so.

    B. Navigate to Project Directory

    C. run Migrations.
        * Run command:
            + python3 manage.py makemigrations blogapp
            + python3 manage.py migrate
            + python3 manage.py runserver
        



