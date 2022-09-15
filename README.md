# I Love This Game

[View the live project here.](https://i-love-this-game.herokuapp.com/)

This is a blog dedicated to old-school/retro/vintage NBA (National Basketball Association), specifically about the 80s/90s era, the best years in the history of American basketball. It's a space of discussion where opinions and information can be shared in a healthy way, but it's mostly meant to be a nostalgic and beautiful trip down memory lane and a celebration of this sport. It’s designed to be a simple-to-use and functional app, and also responsive and accessible on a range of devices, making it easy to navigate for NBA fans.

![Am I Responsive](docs/am-i-responsive.png)

## User Experience (UX)

### • User Stories

#### As a user, I can:

o click on the social media links in the footer so that I can follow the blog's presence on social media and interact with the NBA community and the blog's administrators

o access a page on the blog where I can create a post so that I can write my posts

o update my blog posts so that I'm in control of my posts only

o delete my posts so that I can decide if I want to keep my posts on the blog or not

o see the blog's posts ordered by date so that I can see the most recent ones first

o register on the blog so that I can log in every time I want to post something

o look for posts by category so that I can easily access any specific posts I may look for

o access a page where I can add a new category for my posts so that it's easier for the other users to find them

o don't want any other users to be able to edit my posts, and I shouldn't be able to edit other users' posts either

o log in so that I can create posts of my own

o click on any post's like button so that I can like posts

o click on any post's unlike button so that I can unlike posts

o use my first name or may last name or may email address so that I can register

o look at the snippet of any post so that I know what it's about without having to click on it to read it

o use the edit settings page so that I can update my settings

o use the options on the settings page so that I can easily update my settings

o access a password page on the blog so that I can change my password without having to use the admin page

o upload a header image for any post of mine so that my posts are easy to identify

o add a profile picture and social media links to my profile so that I make it more complete and this information is visible to any users who read each of my posts

o add a profile picture so that it's visible on each of my posts

o create my profile on my own profile page so that the info is visible on my posts

o access an edit profile page so that I can edit my profile

o access and complete a form on the blog so that I can create and edit my profile

o see all the comments on any post so that I can read them

o fill out a comment form so that I can comment on any posts

o complete an easy-to-use form to log in so that I can use the blog as a logged-in user

o check if my name is on the right-hand side of the navbar so that I know if I'm logged in or not

o submit a simple form so that I can send a private message to the administrator of the blog, who will see the message on the admin area

o click on the about link on the navbar so that I can access the about section of the blog and find out more about it and its developer

o perform any action I'm allowed to when using the blog and be informed each time so that I know that my actions were performed

o and though I'm a person with disabilities, I'm able to use the blog's features so that I can access the blog as easily as users who do not have special needs do

#### As a developer, I can:

o set up the project and deploy it for the first time so that everything works before creating any code

o create a Django superuser for the admin area so that I have control of what is posted on the blog

o use Django class-based views to create webpages out of blog posts so that every post can be seen by the user on a page dedicated to that post

o use class-based generic views so that I can add site pagination

o use Bootstrap to create and style the blog so that it looks more appealing to the user

o use Bootstrap so that I can style the backend form

o create functionality that allows the users to look for posts by category so that the users can easily access any specific posts they may look for

o create slug URLs for the category pages so that every post has a unique URL

o add bio fields to the Profile model so that these options will be available to users

o add an image to the Home page so that the user can view it when accessing the page's content and have a better, more pleasant visual experience

o want to test all features of the blog so that any bugs are found and fixed before the final deployment

o want to create the blog's README.md file so that all details of its creation are documented

### • Design

#### o Color Scheme

This is a blog about the NBA, so it made sense to add the NBA colors (blue, red and white) to it, mainly using the logo image and the image on the Home page, so the users can immediately identify what the blog is about (the NBA's logo is known worldwide, even most people who are not into basketball will have seen it before). The dark color used on the navbar and the footer is from Bootstrap's "bg-dark" class (#343a40) and aims to emulate [the NBA's official website's navbar](docs/nba-official-website-navbar.png) and footer: a dark background color with white text and light grey text, which becomes lighter when hovered over by the user for better readability and accessibility. All content is written on a white background using black-colored text, the perfect contrast for any amount of text when it comes to readability and accessibility, also used by the NBA's official website. The links have the normal hyperlink blue color, which happens to match the blue NBA color, and the same applies to all the buttons on the body of the blog's pages created for users to action something (this blue color is from Bootstrap's "btn-primary" class).

Please see the results for the body's color contrast check [here](docs/color-contrast-check-body.png).
Please see the results for the navbar's and the footer's color contrast check [here](docs/color-contrast-check-navbar-and-footer-white-text.png) and [here](docs/color-contrast-check-navbar-and-footer-light-grey-text.png).

#### o Typography

Roboto is the font used in the NBA'S official website, it suits the layout and the style of this blog and provides clear reading and accessibility for the user, so it was used as part of a [system font stack already available on the user's machine](docs/system-font-stack.png), which is believed to be a useful and elegant solution that eliminates the need to fetch a font elsewhere and makes load times faster (fonts are usually one of the heaviest resources loaded on any app). It matches what the current Operating System uses, so it lends a comfortable look to this project. It was imported along with the Bootstrap code used throughout the blog.

#### o Imagery

Very much on purpose, there are not many images on this blog. The two images used - [the one on the Home page](theblog/static/images/home-image.png) and [the one on the navbar's logo](theblog/static/images/logo.png) - do much of the work helping the user identifying what this project is about and providing color/style to the first page the user sees when he/she lands on the blog (the colors of the NBA - blue, red and white - are crucial here). Users can upload a photo to their profile, and they can upload an image to every single post they create, so many images decorating this blog's articles are to be expected in the future (Cloudinary is the image-hosting service used to upload images for this project). There's also a [no-profile-icon image](theblog/static/images/no-profile-photo-icon.png), which is added as a photo to profiles where the user hasn't uploaded his/her/a photo. And, of course, there's [the favicon image](theblog/static/images/favicon-basketball.png) used for this blog (very appropriately, a basketball).

### • Wireframes

o Desktop wireframe (Home 1 - user logged out page) - [View](docs/wireframes/home-1-user-logged-out-page-desktop.png)

o Desktop wireframe (Home 2 - user logged out page) - [View](docs/wireframes/home-2-user-logged-out-page-desktop.png)

o Desktop wireframe (About page) - [View](docs/wireframes/about-page-desktop.png)

o Desktop wireframe (Categories page) - [View](docs/wireframes/categories-page-desktop.png)

o Desktop wireframe (Register page) - [View](docs/wireframes/register-page-desktop.png)

o Desktop wireframe (Log in page) - [View](docs/wireframes/log-in-page-desktop.png)

o Desktop wireframe (Home 1 - user logged in page) - [View](docs/wireframes/home-1-user-logged-in-page-desktop.png)

o Desktop wireframe (Home 2 - user logged in page) - [View](docs/wireframes/home-2-user-logged-in-page-desktop.png)

o Desktop wireframe (Create Article page) - [View](docs/wireframes/create-article-page-desktop.png)

o Desktop wireframe (Article page) - [View](docs/wireframes/article-page-desktop.png)

o Desktop wireframe (Update Article page) - [View](docs/wireframes/update-article-page-desktop.png)

o Desktop wireframe (Delete Article page) - [View](docs/wireframes/delete-article-page-desktop.png)

o Desktop wireframe (Create Comment page) - [View](docs/wireframes/create-comment-page-desktop.png)

o Desktop wireframe (Create Category page) - [View](docs/wireframes/create-category-page-desktop.png)

o Desktop wireframe (Contact page) - [View](docs/wireframes/contact-page-desktop.png)

o Desktop wireframe (Update Settings page) - [View](docs/wireframes/update-settings-page-desktop.png)

o Desktop wireframe (Update Password page) - [View](docs/wireframes/update-password-page-desktop.png)

o Desktop wireframe (Create Profile page) - [View](docs/wireframes/create-profile-page-desktop.png)

o Desktop wireframe (Show Profile page) - [View](docs/wireframes/show-profile-page-desktop.png)

o Desktop wireframe (Update Profile page) - [View](docs/wireframes/update-profile-page-desktop.png)

o Mobile wireframe (Home - user logged out page) - [View](docs/wireframes/home-user-logged-out-page-mobile.png)

o Mobile wireframe (About page) - [View](docs/wireframes/about-page-mobile.png)

o Mobile wireframe (Categories page) - [View](docs/wireframes/categories-page-mobile.png)

o Mobile wireframe (Register page) - [View](docs/wireframes/register-page-mobile.png)

o Mobile wireframe (Log in page) - [View](docs/wireframes/log-in-page-mobile.png)

o Mobile wireframe (Home - user logged in page) - [View](docs/wireframes/home-user-logged-in-page-mobile.png)

o Mobile wireframe (Create Article page) - [View](docs/wireframes/create-article-page-mobile.png)

o Mobile wireframe (Article page) - [View](docs/wireframes/article-page-mobile.png)

o Mobile wireframe (Update Article page) - [View](docs/wireframes/update-article-page-mobile.png)

o Mobile wireframe (Delete Article page) - [View](docs/wireframes/delete-article-page-mobile.png)

o Mobile wireframe (Create Comment page) - [View](docs/wireframes/create-comment-page-mobile.png)

o Mobile wireframe (Create Category page) - [View](docs/wireframes/create-category-page-mobile.png)

o Mobile wireframe (Contact page) - [View](docs/wireframes/contact-page-mobile.png)

o Mobile wireframe (Update Settings page) - [View](docs/wireframes/update-settings-page-mobile.png)

o Mobile wireframe (Update Password page) - [View](docs/wireframes/update-password-page-mobile.png)

o Mobile wireframe (Create Profile page) - [View](docs/wireframes/create-profile-page-mobile.png)

o Mobile wireframe (Show Profile page) - [View](docs/wireframes/show-profile-page-mobile.png)

o Mobile wireframe (Update Profile page) - [View](docs/wireframes/update-profile-page-mobile.png)

### • Data Model

The data model for this project was built using Excel. A screenshot of the spreadsheet was then converted into an image file and has been made available on this README.md file. It makes extensive use of Django's built-in User model.

Five models were created for this project. Being a blog, the Post model (with all the necessary fields for the blog's posts, linked to the Category and User models through ForeignKeys and, again, to the User model through a ManyToManyField relationship, as a post can have many likes by many users) and the Comment model (with all the necessary fields for all posts' comments, linked to the Post and User models through ForeignKeys) were obvious choices, but there are also the Category model (with all the necessary fields for the blog's posts's categories - the Post model is linked to it through a ForeignKey) and the Profile model (with all the necessary fields for the users' profiles, linked to the User model through a OneToOneField relationship, as a user has only one profile - this model and all of its functionality is kept in a separate app specifically created for this purpose, the "members" app, for a better understanding of the blog's code and its many functionalities, as all other models are kept in the "theblog" app) - these four models were created based on John Elder's video tutorial on how to create a blog with Python and Django on YouTube (it can be found [here](https://www.youtube.com/watch?v=B40bteAMM_M)) and tweaked in order to meet the needs of this project and the ideas of its creator. The fifth model is an original idea by the creator of this blog, as some sort of direct/private contact between the blog's logged-in users and the site administrator was necessary - it's also kept in the "theblog" app.

Object-Oriented Programming and Django’s class-based views were widely used throughout this project but, in a few specific blocks of code, function-based views were also used.

![Model Diagram](docs/model-diagram.png)

### • Agile Project Planning

This project was planned and carried out using an Agile approach. 45 User Stories were created based on the idea of building a basketball blog by the creator of this project, and the planning of each step in the Agile plan of action used was done based on John Elder's video tutorial on how to create a blog with Python and Django on YouTube (it can be found [here](https://www.youtube.com/watch?v=B40bteAMM_M)) - it greatly helped organizing the thinking and prioritization of the User Stories and tasks that let to the final product that is I Love This Game.

Each User Story was created on GitHub using a User Story template created for this purpose (each step of this Agile plan was created on GitHub, for that matter). The User Stories were then transferred to a Product Backlog, created using the "Milestones" tab, and refined/re-prioritized as needed.

The MoSCoW technique (MUST-have, SHOULD-have, COULD-have, WON'T-have) was then used to add one of these specific labels to each of the User Stories based on the User Story's importance to the project - these labels were also created using the "Milestones" tab.

Then, a Project called "I Love This Game Blog User Stories" was created and, inside it, a Kanban Board, where all the User Stories were again transferred to. This simple Kanban Board has three columns - "Todo", "In Progress" and "Done" - and the User Stories would go from the "Todo" column to the "In Progress" column when they were being worked on. This was a huge help when tracking progress of what had been done and what still needed to be done throughout the project. When the User Story's tasks were performed and the User Story functionality was implemented, it would be finally moved to the "Done" column. This was basically how this project was planned and built. The Kanban Board for this project can be found [here](https://github.com/users/PedroMiguelFerreira/projects/4/views/1) - only one COULD-have User Story was not implemented on this iteration, but it might be in the future.

## Features

• Favicon

o The favicon for this blog - very appropriately, a basketball - is visible on browser tabs to help users identifying and the blog.

![Favicon](docs/favicon.png)

• Navigation Bar

o Built using Bootstrap and featured at the top of every page on this blog, this fully responsive navigation bar (the user can click on the hamburger menu - three bars - in the top right corner to toggle the menu when using it in smaller devices) introduces the user to all the specific content on the app - when the user is not logged in, it shows links to the About page, a Categories dropdown menu with links to all the post categories, the Register page and the Log in page. When the user is logged in, it shows links to the About page, a Categories dropdown menu with links to all the post categories, the Create Article page, the Create Category page, the Contact page and, at the far-right, the name of the logged-in user (meaning that the user is logged in), which shows a dropdown menu with links to the Update Settings page, the Update Profile page, the Show Profile page and a link for the user to log out - when the user has no profile created yet, the dropdown menu of the name of the logged in user shows the same links except for the Update Profile page and the Show Profile page, which are replaced with a link to the Create Profile page.

o It's a sticky navigation bar, so it follows the user's viewport as he/she scrolls up and down each page of the blog, allowing the user to easily navigate through the content across all devices without having to go back to the top of the page to access other sections of the website. There's a highlight effect to each link on the navbar while being hovered over.

o It also contains the blog's slogan, which brings the user to the Home page when clicked on, and an NBA image with its logo (non-clickable) for styling and to easily state what the blog is about.

**When the user is logged out:**

Navbar:

![Navbar when the user is logged out](docs/navbar-user-logged-out.png)

Categories dropdown menu:

![Categories dropdown menu](docs/categories-dropdown-menu.png)

**When the user is logged in:**

Navbar:

![Navbar when the user is logged in](docs/navbar-user-logged-in.png)

Categories dropdown menu:

![Categories dropdown menu](docs/categories-dropdown-menu.png)

User-logged-in dropdown menu (when the user previously created a profile):

![User-logged-in dropdown menu when the user previously created a profile](docs/user-logged-in-dropdown-menu-profile-created.png)

User-logged-in dropdown menu (when the user hasn't previously created a profile):

![User-logged-in dropdown menu when the user hasn't previously created a profile](docs/user-logged-in-dropdown-menu-no-profile-created.png)

• Footer

o Built using Bootstrap, the footer includes a "Copyright © 2022 Pedro Ferreira" notice – it’s shown on every page of the website (it's a sticky footer, so it follows the user's viewport as he/she scrolls up and down every page on this blog). 

o The social media icons on it (for YouTube, Instagram, Twitter and Facebook) lead the user to the official social media pages for the NBA (as the creator of this blog has chosen not to make his social media accounts public at this stage).

o There's a highlight effect to each social media icon on the navbar when hovered over.

o Any external links will open in a new tab to allow easy navigation for the user and avoiding the user to leave the website.

![Footer](docs/footer.png)

• Home page

o The Home page works as the landing page, and its the first thing the user sees on this blog. It has a beautiful image of a slightly transformed NBA logo (for copyright purposes) at the top, to make the user aware it's a basketball website, and the NBA colors lend a sports feeling to the whole thing.

o By scrolling down, the user will see the most recent posts created by the blog's users. A button was added at the bottom of the page to go to the next page of posts (with older posts) - there are five posts per page so it doesn't get too crowded and the pages breathe better. Every post's details are visible (title, author, category, date, etc.), and the user can click on the title to view the post and on the category name to see a list of other posts belonging to the same category. If the user is the author of any given post, that post will have links to update/delete the post.

![Home 1](docs/home-page-1.png)

![Home 2](docs/home-page-2.png)

![Home 3](docs/home-page-3.png)

• Article page

o Every post page has the title at the top, along with the author's name and the date it was posted. It can be accessed by any user, logged in or not. There's also a back button to the Home page (many pages on this blog have one for an easier user navigation) in case the user wants to leave the page with no further action.

o Any external links will open in a new tab to allow easy navigation for the user and avoiding the user to leave the website.

o There's a like button for logged-in users to like/unlike the post, and also the profile of the post's author, which can be accessed by any user.

o There's also a comments section at the bottom of the page, with all the comments for the post - if the user is logged in, it can create a comment for the post.

![Article 1](docs/article-page-1.png)

![Article 2](docs/article-page-2.png)

• Create Article page

o If the user is logged in, he/she can create a post. It's a simple form, with a few fields to easily create a post, like title, title tag, category, body, snippet and an image field, which is the only one that is not mandatory.

o Once created, the user sees a confirmation message and is redirected to the Home page where he/she'll be able to see his/her post as the most recent post.

![Create Article 1](docs/create-article-page-1.png)

![Create Article 2](docs/create-article-page-2.png)

• Update Article page

o If the user is logged in, he/she can update his/her own posts by clicking on the "Update" link on the post itself.

o Once updated, the user sees a confirmation message and is redirected to the page of the updated post.

![Update Article 1](docs/update-article-page-1.png)

![Update Article 2](docs/update-article-page-2.png)

• Delete Article page

o If the user is logged in, he/she can delete his/her own posts by clicking on the "Delete" link on the post itself.

o Before deletion is done, the user is asked to confirm if he/she really wish to delete the post (extra confirmation in case it's not what the user wants to do).

o Once updated, the user is redirected to the Home page where he/she'll be able to see that his/her post is no longer there.

![Delete Article](docs/delete-article-page.png)

• About page

o A page that can be accessed by any users, logged in or not. It's an introduction to the blog and a description of the basketball era it aims to represent. It also contains an "Acknowledgements" sub-section, where the creator of this blog has thanked Bill Simmons and John Elder for their work, parts of which have been used as a base for this project.

o Any external links will open in a new tab to allow easy navigation for the user and avoiding the user to leave the website.

![About](docs/about-page.png)

• Categories page

o A page that can be accessed by any users, logged in or not. The link on the navbar will show a dropdown menu with a list of categories created by users on the blog itself and the blog administrator - the user can choose to view posts from any category and, by clicking on the desired category, he/she'll be taken to a page with the list of posts for that category.

o When there are no posts for a specific category, the user will be brought to a page saying that there are currently no posts for that category.

![Categories 1](docs/categories-page-1.png)

![Categories 2](docs/categories-page-2.png)

![Categories 3](docs/categories-page-3.png)

• Register page

o A page that can be accessed by users who are logged out and/or haven't registered yet (they need to register in order to be able to log in and use all the blog's features as logged-in users).

o Once the user registers (there's a back button in case he/she has second thoughts), he/she sees a confirmation message and will be redirected to the Log In page so the user can finally log in.

![Register 1](docs/register-page-1.png)

![Register 2](docs/register-page-2.png)

• Log In page

o This is the page where the user can log in and have access to all the blog's functionality - once the user logs in, his/her name wil show up at the far-right of the navbar.

![Log In 1](docs/log-in-page-1.png)

![Log In 2](docs/login-page-2.png)

• Create Category page

o If the user is logged in, he/she can create a new category by completing the simplest of forms.

o Once the category is created, the user sees a confirmation message and is redirected to the Home page.

![Create Category 1](docs/create-category-page-1.png)

![Create Category 2](docs/create-category-page-2.png)

• Contact page

o If the user is logged in, he/she can contact the blog administrator directly by completing and sending a simple form. The blog administrator will receive it and view it in the admin area. There's no functionality for the administrator to reply to these messages via the admin area at this stage (maybe in the future).

o Once the message is sent, the user sees a confirmation message and is redirected to the Home page.

![Contact 1](docs/contact-page-1.png)

![Contact 2](docs/contact-page-2.png)

• Update Settings page

o If the user is logged in, he/she can update the settings on their account/profile on this page. Here, the user can also access a link to change his/her password.

![Update Settings](docs/update-settings-page.png)

• Update Password page

o If the user is logged in, he/she can update his/her password using the link on their Update Settings page.

o Once the password is updated, the user sees a confirmation message AND is redirected to a password success page, with a button that will redirect the user to the Home page when clicked on - two kinds of user action confirmation to show two ways of informing the user of a successful action.

![Update Password 1](docs/update-password-page-1.png)

![Update Password 2](docs/update-password-page-2.png)

• Create Profile page

o If the user is logged in, but doesn't have a profile yet, he/she can create one on this page.

o The only mandatory field is the bio, the rest can be added to the profile or not by the user. Any fields not used will not show up on the user's profile (photo, social media accounts, etc.).

o Once the profile is created, the user sees a confirmation message and is redirected to the Home page.

![Create Profile 1](docs/create-profile-page-1.png)

![Create Profile 2](docs/create-profile-page-2.png)

• Update Profile page

o If the user is logged in and already has a profile, he/she can update it one on this page.

o Once the profile is updated, the user sees a confirmation message and is redirected to the Home page.

![Update Profile 1](docs/update-profile-page-1.png)

![Update Profile 2](docs/update-profile-page-2.png)

• Show Profile page

o If the user is logged in and already has a profile, he/she can view it on this page.

![Show Profile](docs/show-profile-page.png)

• Login Error pages

o Whenever the user makes a mistake logging in - for example, opens any link of the blog on a separate tab, logs out on that separate tab and comes back to the first page it opened (where he/she's technically still logged in) and tries to access any page there, he/she won't be able to and a login error page will be shown to the user.

![Login Error 1](docs/log-in-error-page-contact.png)

![Login Error 2](docs/log-in-error-page-create-article.png)

![Login Error 3](docs/log-in-error-page-create-category.png)

![Login Error 4](docs/log-in-error-page-create-profile.png)

![Login Error 5](docs/log-in-error-page-delete-article.png)

![Login Error 6](docs/log-in-error-page-update-article.png)

![Login Error 7](docs/log-in-error-page-update-profile.png)

o If the user opens any link of the blog on a separate tab ("Update Article", for example, to update a specific article), logs out on the first page it opened, goes back to the page it opened on a separate tab (where he/she's technically still logged in) and tries to continue and finish his/her action there, he/she will be able to do so, but only that specific action (in this case, to update a specific article) and only once (if the URL of this action page is copied and opened in a third tab, the login error page for "update article" will be shown to the user) - as soon as the article is updated, the user sees a confirmation message saying that the article was updated, but he/she will be automatically logged out and will have to login to access any other part of the blog only accessible by logged-in users - if the user tries to access any part of the blog only accessible to logged-in users without logging in, he/she won't be able to and one of the login error pages shown above will be shown to the user.

• Admin area

o In the admin area (to which only the superuser/blog administrator has access), the administrator can control the content of the blog as well what its users do on it.

o The admin user has access to more functionality than regular users, which allows them to create, read, update and delete information such as users, categories, comments, profiles, messages, posts and profiles.

o As mentioned before, only the superuser/blog administrator can access the admin area, and he can do so by adding "/admin" to the URL of the Home page and signing in.

![Show Profile](docs/admin-area.png)

## Features Left to Implement

• A Media page, with YouTube iFrames of old NBA videos from the 80s and 90s. "NBA Action", "I Love This Game", etc.... It would be a great add to this blog. This was one of two User Stories that were created, but not implemented in the final version of the project.

• A rich-text editor to stylize the blog posts - CKEditor was actually implemented, but created so many issues with Cloudinary and the database that it was removed from the project at this stage. Maybe in a future iteration. This was the second of two User Stories that were created, but not implemented in the final version of the project.

• Functionality that allows the user to delete a category created by himself/herself (on this iteration, the user is only allowed to create a category, not delete it).

• Functionality that allows the blog administrator to reply to the contact messages sent via the frontend by registered users. A view showing all the received messages (which is only accessible by the blog administrator) would have to be shown (something like Gmail's inbox, with a card or something similar for each message showing the sender's name and subject). Then, clicking on a message would take us into a message detail view, where we would be able to see the full message body - there would also be a form on that page, where the blog administrator could type a reply into.

• Functionality that allows the user to update/add an image to his/her post and change the category when updating it (every other field can be updated).

• Reply to post comments in a thread, like in Facebook, for example.

## Technologies Used

### Languages Used

• [HTML5](https://en.wikipedia.org/wiki/HTML5)

• [CSS3](https://en.wikipedia.org/wiki/CSS)

• [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

• [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries, Programs, Databases & Other Tools Used

• [Django](https://en.wikipedia.org/wiki/Django_(web_framework)): Python framework used to create the backend logic

• [Bootstrap 4.4.1](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)): CSS framework used to create the frontend and for responsiveness on all devices

• [jQuery](https://en.wikipedia.org/wiki/JQuery): it came with Bootstrap, along with Popper and Bootstrap JS, to make, for example, the navbar responsive and allow for the dropdown menus to work

• [SQLite](https://en.wikipedia.org/wiki/SQLite): used as the database during development

• [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL): used as the database on deployment

• [Font Awesome](https://fontawesome.com/): used on the footer to add social media icons for aesthetic and UX purposes

• [Git](https://git-scm.com/): used for version control by utilizing the Gitpod (the IDE used) terminal to commit to Git and push to GitHub

• [GitHub](https://github.com/): used to store the project's code after being pushed from Git

• Snipping tool: A snipping tool was used to create the logo and resizing/editing the photos/images for the blog

• [TinyPNG](https://tinypng.com/): used to compress all four photos/images on the blog

• [Balsamiq](https://balsamiq.com/): used to create the wireframes during the design process

• [WebAIM](https://webaim.org/resources/contrastchecker/): used as a contrast checker for the colors used on the blog

• [Heroku](https://www.heroku.com/): used to deploy the live project

• [Microsoft Excel](https://en.wikipedia.org/wiki/Microsoft_Excel): used to create the model diagram during the design process

• [Chrome DevTools](https://developer.chrome.com/docs/devtools/): used to debug the blog and test responsiveness

• [Cloudinary](https://en.wikipedia.org/wiki/Cloudinary): the image-hosting service used to upload the images of the blog

• [GitHub Projects](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/tracking-work-with-project-boards): used for the Agile planning and tracking of the project

## Testing

### Validation Testing

The W3C Markup Validator Service, the W3C CSS Validator Service, the JSHint Static Code Analysis Tool for JavaScript and the PEP8 Online Checker were used to validate every page of this project to ensure there were no syntax errors.

• W3C Markup Validator (results)

 [about](docs/html-validator-results-about.png)

 [add_category](docs/html-validator-results-add-category.png)

 [add_comment](docs/html-validator-results-add-comment.png)

 [add_post](docs/html-validator-results-add-post.png)

 [categories](docs/html-validator-results-categories.png)

 [category_list](docs/html-validator-results-category-list.png)

 [change_password](docs/html-validator-results-change-password.png)

 [contact](docs/html-validator-results-contact.png)

 [create_user_profile_page](docs/html-validator-results-create-user-profile-page.png)

 [delete_post](docs/html-validator-results-delete-post.png)

 [edit_profile_page](docs/html-validator-results-edit-profile-page.png)

 [login](docs/html-validator-results-login.png)

 [password_success](docs/html-validator-results-password-success.png)

 [update_post](docs/html-validator-results-update-post.png)

 [user_profile](docs/html-validator-results-user-profile.png)

 [edit_profile](docs/html-validator-results-edit-profile.png)
 There are three errors on this page when validation is ran - this is because a UserChangeForm was imported from django.contrib.auth.forms and used to create the content of this page, so it's a Django backend thing and can't be changed.

 [register](docs/html-validator-results-register.png)
 There are four errors on this page when validation is ran - this is because a UserCreationForm was imported from django.contrib.auth.forms and used to create the content of this page, so it's a Django backend thing and can't be changed.

 [article_details](docs/html-validator-results-article-details.png)

 [base](docs/html-validator-results-base.png)

 [home](docs/html-validator-results-home.png)

• W3C CSS Validator - [Results](docs/css-validator-results.png)

• JSHint - [Results](docs/javascript-validator-results.png)

• PEP8 Online Checker (results)

Only .py pages that were created/changed by the creator of this project were validated using PEP8.

[I Love This Game - settings.py](docs/python-validator-results-i-love-this-game-settings-py.png)
There was an error message in the terminal on this file ("env imported but unused"), but I was advised by my mentor to leave it in the code as it's not possible to access the 8000 Portal without it and explain it here (and Matt Rudge added this to his code on the Codestar walkthrough). Also, # NOQA was added to four lines on this file as well as they were too long and it wasn't possible to make them shorter (the code was also not created by the creator of this project - it's in the auth_password_validators, a section that was automatically created). Anyway, all the code on this file passed PEP8 validation with no errors.

[I Love This Game - urls.py](docs/python-validator-results-i-love-this-game-urls-py.png)

[Members - forms.py](docs/python-validator-results-members-forms-py.png)

[Members - urls.py](docs/python-validator-results-members-urls-py.png)

[Members - views.py](docs/python-validator-results-members-views-py.png)

[Theblog - admin.py](docs/python-validator-results-theblog-admin-py.png)

[Theblog - forms.py](docs/python-validator-results-theblog-forms-py.png)

[Theblog - models.py](docs/python-validator-results-theblog-models-py.png)
There were five error messages in the terminal on this file, but I was advised by my mentor to leave them in the code as they made no sense, the code was correct and these were just runtime errors. Anyway, all the code on this file passed PEP8 validation with no errors.

[Theblog - urls.py](docs/python-validator-results-theblog-urls-py.png)

[Theblog - views.py](docs/python-validator-results-theblog-views-py.png)
There were four error messages in the terminal on this file, but I was advised by my mentor to leave them in the code as they made no sense, the code was correct and these were just runtime errors. Anyway, all the code on this file passed PEP8 validation with no errors.

env.py - Because this is where the secret environment variables are kept, a screenshot of this validation was not included on the README.md file. Also, # NOQA was added to two lines on this file as they were too long and it wasn't possible to make them shorter (they're secret keys, very long lines of numbers). Anyway, all the code on this file passed PEP8 validation with no errors.

[manage.py](docs/python-validator-results-manage-py.png)

[reset.py](docs/python-validator-results-reset-py.png)

The Am I Responsive? website design tester was used to test the responsiveness of this website. [Screenshot here](docs/am-i-responsive.png)

Google Chrome's DevTools were used to thoroughly test this website, including the Lighthouse tool - please see below screenshots of both Lighthouse reports (one for Desktop and one for Mobile).

The "83" in "Best Practices" for both Desktop and Mobile is due to, according to Lighthouse, the images being displayed with the incorrect ratio (it has to do with the dimensions of the images) and a low resolution (it has to do with the images' natural dimensions and the size they're being displayed), and the logo image is the image referenced on the report, but it's supposed to be this size (it was resized to be displayed exactly like this, though the report says the width and the height haven't been set, but they have), and it was compressed (all images have) to decrease page load time, as it should be. Also according to Lighthouse, another reason for the "83" in "Best Practices" for both Desktop and Mobile is the frontend JavaScript libraries with known security vulnerabilities - jQuery was referenced as the issue, but this library is necessary for, for example, the dropdown menus in the navbar, so it has to be on the code.

The "71" in "Performance" for mobile is due to, according to Lighthouse, the image elements not having explicit width and height, but they do; the image format used for the Home and Logo images (as well any other images) was PNG, and Lighthouse mentions that formats like WebP and AVIF often provide better compression than PNG, which would mean faster downloads and less data consumption but, on this occasion, it was decided that all images should be in PNG format, as compression is lossless, meaning that there's no loss in quality each time a file is opened and saved again, and PNG is also good for detailed/high-contrast images. The issue with properly sized images, incorrect ratio and low resolution (for the Home and Logo images again) is also mentioned on the report for Mobile, and was explained in the above paragraph for "Best Practices" already. Another reason for this low score on Mobile is, according to Lighthouse, the use of Bootstrap for JS and CSS, but these are necessary to make the blog work properly, so they have to be part of the code. The same is mentioned on the report for Mobile in relation to the Font Awesome Kit used on the code but, again, it needs to be there.

[Desktop](docs/lighthouse-report-desktop.png)

[Mobile](docs/lighthouse-report-mobile.png)

### Testing User Stories from the User Experience (UX) Section

During development, each User Story was manually tested countless times, but the following table tracks the final manual testing of each User Story after deployment:

![Testing User Stories 1](docs/testing-user-stories-1.png)

![Testing User Stories 2](docs/testing-user-stories-2.png)

![Testing User Stories 3](docs/testing-user-stories-3.png)

![Testing User Stories 4](docs/testing-user-stories-4.png)

### Further Testing

• The blog was tested on the Google Chrome, Mozilla Firefox and Microsoft Edge browsers by the creator of this blog. It was not tested on Internet Explorer as it's no longer supported, but was tested on the Safari browser by friends and family, and the feedback was good.

• The website was viewed on a variety of devices such as large laptops, medium/smaller laptops, tablets, phablets, larger mobile phones and medium/smaller mobile phones - it was fully responsive in all of them.

• A large amount of testing was done to ensure that all links on the blog were linking correctly. The same was done for all the external links, including the social media icons on the footer. All features and functionality were also tested on all possible devices.

• Friends, family members and NBA fans were asked to review the site and documentation to point out any bugs and/or user experience issues - feedback was good.

### Security

• All secret keys are stored in the env.py file, which was added to the .gitignore file, to prevent unwanted connections to the database - this was set up before the first push to GitHub.

• There's a runtime.txt file that is visible in the GitHub repository - this was created together with Tutor Support after the initial setup as there were errors in the terminal preventing git adding/committing/pushing due to a conflict with the Django version being used. This runtime.txt file fixed the issue, and the creator of this blog was advised by his mentor that there was no need to hide it.

• The db.sqlite3 file is visible in the GitHub repository, too - again, the creator of this blog was advised by his mentor that there was no need to hide it.

• The reset.py and theblog.json files are visible in the GitHub repository, too - again, the creator of this blog was advised by his mentor that there was no need to hide them. These files were used to fix some of the several issues that the creator of this blog had with corrupt databases throughout the creation of this project - Tutor Support, on separate occasions, brilliantly came up with the idea to use these files to reset the database and not losing information (like Categories, Articles, Comments, Contacts, etc.). There's no secret information in them, so there was no need to hide them (and the creator of this blog was actually advised to keep them just in case).

• DEBUG was set to False right before deployment to prevent access to error screens and code.

• Registration/authentication was set up to ensure that only logged-in users and authors can update/delete their own articles and not other users' articles.

• Cross-Site Request Forgery (CSRF) tokens were used on the forms to prevent requests to the backend server being created for malicious purposes.

• Django handles most of the defensive design used to make sure users can't submit empty fields on forms, etc. - where necessary, of course: some fields are mandatory, some aren't, like a photo or social media links when creating a user profile, for example.

### Known Bugs

#### Fixed Bugs

Countless bugs were found and fixed during the creation of this blog - the list is long, but here are the most memorable ones:

• A runtime.txt file (with python-3.8.11 in it) had to be created to allow to git push to GitHub

• pip3 install 'django<4' gunicorn was not used during the initial setup (pip3 install django gunicorn was incorrectly used), so the incorrect version of Django installed (Django-4.1) was preventing me to access Django's admin area (403 error), so it had to be uninstalled, the correct one (django==3.2) had to be installed and the requirements.txt file had to be updated

• JavaScript was used to restrict the add_post.html page to only allow logged-in users to create posts in their own name, not another user's name - JavaScript was used to add user.id to the Create Article form automatically; CSS code on the style.css file was used to to hide the user.id on the Create Article page. Tutor Support's help was particularly useful here.

• When the logged-in user was in a page with posts belonging to a specific category, he/she could see the option to update and delete all posts, not just his/hers as it should; adding {% if user.id == post.author.id %} to the authentication section on the categories.html page fixed this.

• Users that were not logged in could see the option to comment on any posts, and could indeed comment on them; adding {% if user.is_authenticated %} to the relevant links on the Comments section of the article_details.html page fixed this.

• HTML showing on the article's snippet when articles were viewed on the list of articles of a specific category; this was fixed by adding the safe HTML tag to the categories.html page (later removed due to the removal of the CKEditor functionality from the project).

• The "author" field was visible on the Contact form when the logged-in user was filling it out, and the user could choose the username to add to the form, which shouldn't happen - the "author" field was removed from the ContactCreateView and a method to add the request user was added, and this fixed the issue. Tutor Support's help was particularly useful here.

• Posts created by users who didn't create a profile couldn't be viewed by any user; this was fixed by removing the word "profile" from the URL on the Profile section of the article_details.html. Tutor Support's help was particularly useful here.

• Users were able to create posts that were empty on the "body" field - this was fixed by changing the blank and null fields on the Post model to False and adding a default message on the body of the post (the placeholder was later removed, as there was no need for it). Tutor Support's help was particularly useful here.

• The logged-in user was being prompted to provide his/her name when commenting on a post, which shouldn't happen; this was fixed by adding form.instance.author = self.request.user to the AddCommentView in the views.py file. Tutor Support's help was particularly useful here.

• Though the user didn't have a profile created, the link to it showed up next to the user's name on the posts he/she created and gave an error message when clicked on; this was fixed by adding an if statement to the profile section of the post.

• There was lack of responsiveness on the Contact, Update Settings and Update profile pages; this was fixed by adding a new media query for small devices.

• There were fields in the "Update Settings" page that allowed the normal user to make himself a superuser and have access to the admin area - changing the form in forms.py by removing these fields solved the problem.

• Categories were not being imported into the Create Post page (this was fixed by changing the model and linking categories to the Post model with a ForeignKey).

• The Comments section on the admin area couldn't be accessed (error message) and the name of the author of a comment would not show next to the comment (this was solved by fixing the author field by adding self.author.username to the Comment model and fixing the string representation).

• The blog's administrator couldn't see the name of the author of a contact sent to the administrator in the admin area (this was solved by fixing the string representation for the Comment model).

• Users were being redirected to the Home page after commenting on a post or after updating one, but they should be redirected to the commented/updated post itself; this was fixed by adding 'article-detail' and the correct object to the get_success_url function for the comment and update post views in views.py.

• The body field on the Create Article page wasn't responsive below 992px - this was because of the CKEditor used on this field at the time (it was later removed from the project); this was fixed by resetting its width with a CSS id rule.

• The placeholder in the body field of the Post model in models.py allowed the user to create a post with just the placeholder as content; this was fixed by removing the placeholder from the code.

#### Unfixed Bugs

• Any success message for deleting a post functionality could not be implemented: for some reason, the creator of this blog was not able to redirect the user to the Home page (as it should be, it's where all the posts are) AND show the confirmation of deletion message on that page at the same time but, after considering it, it might not be a huge fault in the sense that it'll be clear for the user that the post is no longer there (again, the Home page is where all the posts are shown to the user, and the deleted post won't be there anymore) - the creator of this blog hopes the Assessment Team sees it this way, too, and he was advised by his mentor to leave it like this and explain it in this README.md file.
