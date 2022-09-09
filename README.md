# I Love This Game

[View the live project here.]()

This is a blog dedicated to old-school/retro/vintage NBA (National Basketball Association), specifically about the 80s/90s era, the best years in the history of American basketball. It's a space of discussion where opinions and information can be shared in a healthy way, but it's mostly meant to be a nostalgic and beautiful trip down memory lane and a celebration of this sport. It’s designed to be a simple-to-use and functional app, and also responsive and accessible on a range of devices, making it easy to navigate for NBA fans.

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

o style the text of my posts so that I can make them more appealing to read

o look at the snippet of any post so that I know what it's about without having to click on it to read it

o use the edit profile page so that I can create my profile

o use the checkboxes on the profile page so that I can easily create my profile

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

o and though I'm a person with disabilities, I'm able use the blog's features so that I can access the blog as easily as users who do not have special needs do

#### As a developer, I can:

o set up the project and deploy it for the first time so that everything works before creating any code

o create a Django superuser for the admin area so that I have control of what is posted on the blog

o use Django class-based views to create webpages out of blog posts so that every post can be seen by the user on a page dedicated to that post

o use class-based generic views so that I can add site pagination

o use Bootstrap to create and style the blog so that it looks more appealing to the user

o use Bootstrap so that I can style the backend form

o create functionality that allows the users to look for posts by category so that the users can easily access any specific posts they may look for

o create slug URLs for the category pages so that every post has a unique URL

o add a bio field to the User model so that this option will be available to users

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

Very much on purpose, there are not many images on this blog. The two images used - [the one on the Home page](theblog/static/images/home-image.png) and [the one on the navbar's logo](theblog/static/images/logo.png) - do much of the work helping the user identifying what this project is about and providing color/style to the first page the user sees when he/she lands on the blog (the colors of the NBA - blue, red and white - are crucial here). Users can upload a photo to their profile, and they can upload an image to every single post they create, so many images decorating this blog's articles are to be expected in the future (Cloudinary is the image-hosting service used to upload images for this project). And, of course, there's also [the favicon image](theblog/static/images/favicon-basketball.png) used for this blog (very appropriately, a basketball).

### • Wireframes

o Desktop wireframe (Home 1 - user logged out page) - [View](docs/wireframes/home-1-user-logged-out-page-desktop.png)

o Desktop wireframe (Home 2 - user logged out page) - [View](docs/wireframes/home-2-user-logged-out-page-desktop.png)

o Desktop wireframe (About page) - [View](docs/wireframes/about-page-desktop.png)

o Desktop wireframe (Categories page) - [View](docs/wireframes/categories-page-desktop.png)

o Desktop wireframe (Register page) - [View](docs/wireframes/register-page-desktop.png)

o Desktop wireframe (Log in page) - [View](docs/wireframes/log-in-page-desktop.png)

o Desktop wireframe (Home 1 - user logged in page) - [View](docs/wireframes/home-2-user-logged-in-page-desktop.png)

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

o Mobile wireframe (Update Profile page) - [View](docs/wireframes/show-profile-page-mobile.png)





![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome PedroMiguelFerreira,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
