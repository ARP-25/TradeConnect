# TradeConnect - Tradeboard <br>
![titleimage](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701634734/amiresponsive_1_a8dglf.png) 
## Description
TradeConnect  An interactive Django-powered platform designed for traders. Share your trade strategies, engage in insightful discussions, and refine your approach with user ratings and comments. Join us, elevate your trading game, and connect with fellow traders on this vibrant platform crafted for growth and success.

[Click here to view the Live Project](https://tradeconnect-d0f5a2fe7023.herokuapp.com/)

## Table of contents

- [User Experience (UX)](#User-Experience-(UX))
- [Features](#Features)
- [Design](#Design)
- [Technologies Used](#Technologies-Used)
- [Testing](#Testing)
- [Deployment](#Deployment)
- [Credits](#Credits)


## User Experience (UX)

### User stories

- US01 Register/Login to the App

- US02 Create a Trade Post

- US03 Edit a Trade Post

- US04 Search for Trade Post and get a sorted view

- US05 Delete a Trade Post

- US06 Rate a Trade Post

- US07 Inspect detailed Trade Post

- US08 Comment a Trade Post

- US09 Contact Site Owner

## Features

### Existing Features

-  F01 NavBar 
    -   NavBar with Label(redirects to Main Page) and three elements: Home(redirects to Main Page), Login(redirects to Login Page) and Register(redirects to Register Page)
        -   Helps users easily navigate and access various parts of the site
    ![Header](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690782/01_nav_bar_sho6uh.png)  

-  F02 Sign Up Page
    -   Sign Up
    ![SignUp](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690782/02_sign_up_b1lt0o.png) 

-  F03 Login Page
    -   Login
    ![Login](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690782/03_login_nq4vqk.png) 

-  F04 Post Trade Button
    -   Is shifted to Login Button when user is not logged in yet and redirects to Login Page
    -   If logged in redirects to Create Post Page
    ![Post a Trade Button](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/04_post_trade_button_dze2tl.png) 

-  F05 Sort Selection Button
    -   By clicking user is able to sort existing Trade Post's
    ![Sort Selection Button](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/05_sort_selection_button_s6obo6.png) 

-  F06 Trade Post List
    -   Released Trade Post's are found here
    ![Trade Post List](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690780/06_trade_post_list_ra0wf0.png)

-  F07 Pagination Controls
    -   Enhance user experience by simplifying navigation through a vast amount of content. Instead of presenting a long list or a substantial amount of data on one page
    ![Pagination Controls](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/07_pagination_controls_sdiedk.png) 

-  F08 Delete and Edit Button
    -   This feature is available for logged in user's and on their own Trade Post's
    -   Delete: Deletes Trade Post
    -   Edit: Redirects to Edit Trade Post Page
    ![Delete and Edit Button](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/08_delete_edit_hpuvjy.png)

-  F09 Edit Trade Post Page
    -   User is able to take changes on his Trade Post
    ![Edit Trade Post Page](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690779/09_edit_page_smyzlp.png)

-  F10 Detailed Trade Post Page
    -   By clicking on a Trade Post inside the Trade Post List(F06) user gets redirected to Detailed Trade Post Page
    -   Here the user gets a detailed view of the Trade Post, the ability to rate a Trade Post or simply leave a comment
    ![Edit Trade Post Page](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690781/10_detailed_trade_post_page_gcomt8.png)
    -   Commenting
    ![Comments](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690780/10_detailed_trade_post_page_comments_ca64fz.png)
    -   Rating
    ![Rating](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701690780/10_detailed_trade_post_page_rating_hjzfxa.png)

-  F11 Message Form
    -   Site visitors are able to contact the site owner without having to create an account
    ![Edit Trade Post Page](https://res-console.cloudinary.com/dbui0ebjv/thumbnails/v1/image/upload/v1701690780/MTFfbWVzc2FnZV9mb3JtX213aDdjYw==/preview)

### Table of Features and User Stories combined

In this table you can see that every User Story is covered by an implemented Feature.

|     | US 1     | US 2     | US 3     | US 4     | US 5     | US 6     | US 7     | US 8     |  US 9    | 
|-----|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| F 1 |     x    |          |          |          |          |          |          |          |          |
| F 2 |     x    |          |          |          |          |          |          |          |          |
| F 3 |     x    |          |          |          |          |          |          |          |          |
| F 4 |     x    |    x     |          |          |          |          |          |          |          |
| F 5 |     x    |          |          |   x      |          |          |          |          |          |
| F 6 |          |          |          |   x      |          |          |          |          |          |
| F 7 |          |          |          |   x      |  x       |          |          |          |          |
| F 8 |          |          |          |          |  x       |          |          |          |          |
| F 9 |          |          |   x      |          |          |          |          |          |          |
| F10 |          |          |          |          |          |   x      |  x       |      x   |          |
| F11 |          |          |          |          |          |   x      |  x       |      x   |    x     |

### Features which could be implemented in the future

- Ranking System that displays the users with the highest Average Rating on his Trade Post's
- Trading Journal. Should be preferably its own App but in the same Project


## Design
-   ### Styling
    -  For Styling the Bootstrap 5.2.3 library was imported. Additionaly you will find some custom CSS at the top of the style.css file to fit in some custom needs.

-   ### Colour Scheme
    -  The color Scheme is adjusted to mainly provide good contrast and readability but still offers an appealing design and fit the theme of Trading.
    -  The specific areas have the background-color: 
        -   Royal Blue(#4169E1): This color signifies trust, professionalism, and reliability. In the financial and trading sector,         establishing trust is crucial. Royal blue exudes a sense of security, stability, and confidence, which are vital for financial platforms. Black Grey: 
        -   Dark Grey(#333333): Black and shades of grey are often used in conjunction with blue to create a sense of sophistication, seriousness, and elegance. These colors are associated with formality and can convey a professional, sleek appearance.
    -  Font Color is adjusted through the game to give good contrast to specific background-color.

-   ### Typography
    -   Google Fonts was used to import font into styles.css. Montserrat was chosen because it's known for elegance and readability, it's a great choice for conveying a professional tone.

-   ### Wireframes

    ![WireFrames TradeConnect - TradeBoard](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701699587/tradeconnect_figma_n8cjwk.png)

### Database Models

## TradePost

| Field         | Type              | Description                                   |
|---------------|-------------------|-----------------------------------------------|
| title         | CharField         | The title of the trade post.                  |
| slug          | SlugField         | URL-friendly version of the title.            |
| author        | ForeignKey(User)  | Author of the trade post (linked to User).    |
| description   | TextField         | Description of the trade post.                |
| trade_image   | CloudinaryField   | Image associated with the trade post.          |
| created_at    | DateTimeField     | Date and time of creation.                    |
| updated_at    | DateTimeField     | Date and time of the last update.             |
| status        | IntegerField      | Status of the trade post (Draft or Published).|

### Methods:

- `average_rating`: Calculate the average rating based on ratings associated with the trade post.

---

## Rating

| Field    | Type                  | Description                               |
|----------|-----------------------|-------------------------------------------|
| post     | ForeignKey(TradePost) | Trade post associated with the rating.     |
| user     | ForeignKey(User)      | User who rated the trade post.            |
| rating   | IntegerField          | Rating value given to the trade post.     |

---

## Comment

| Field        | Type                  | Description                                      |
|--------------|-----------------------|--------------------------------------------------|
| tradepost    | ForeignKey(TradePost) | Trade post associated with the comment.            |
| name         | CharField             | Name of the commenter.                            |
| email        | EmailField            | Email of the commenter.                           |
| body         | TextField             | Content of the comment.                           |
| created_at   | DateTimeField         | Date and time of creation.                        |
| approved     | BooleanField          | Approval status of the comment (default is True). |

---

## ContactMessage

| Field          | Type       | Description                               |
|----------------|------------|-------------------------------------------|
| name           | CharField  | Name of the sender.                        |
| email          | EmailField | Email of the sender.                       |
| phone_number   | CharField  | Phone number of the sender.                |
| body_message   | TextField  | Content of the message.                    |

---

### Signals:

- `create_slug`: Pre-save signal to generate a slug for a TradePost instance based on its title.


## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Javascript](https://en.wikipedia.org/wiki/JavaScript)
-   [Django Template Language](https://docs.djangoproject.com/en/4.2/ref/templates/language/)
-   [Markdown](https://de.wikipedia.org/wiki/Markdown)


### Frameworks, Libraries & Programs Used

-   [Gitpod:](https://gitpod.io) was used as IDE to create the code. It provides good compatibility with github and offers useful IDE extensions.
-   [GitHub:](https://github.com/) is used as the respository for the projects code after being pushed from Git.
-   [Heroku:](https://heroku.com) was used to deploy the Project.
-   [Django:](https://pypi.org/project/asgiref/)  was used as main Framework for rapid development and pragmatic design.
-   [django-allauth:](https://github.com/pennersr/django-allauth) was used for handling everything from registration to account management.
-   [django-crispy-forms:](https://github.com/django-crispy-forms/django-crispy-forms) was used with Django to easily build, customize, and manage forms using Bootstrap.
-   [django-summernote:](https://github.com/summernote/django-summernote) was used for simple WYSIWYG editing in Django.
-   [gunicorn:](https://pypi.org/project/asgiref/) was used in Django for handling Python WSGI HTTP Server and deployment.
-   [oauthlib:](https://github.com/oauthlib/oauthlib) was used for OAuth request-signing logic.
-   [asgiref:](https://pypi.org/project/asgiref/) was used in Django for handling asynchronous request handling.
-   [dj-database-url:](https://pypi.org/project/dj-database-url/) was utilized for database URLs in settings.
-   [dj3-cloudinary-storage:](https://pypi.org/project/dj3-cloudinary-storage/) was used for custom storage backend for Django using Cloudinary.
-   [psycopg2:](https://pypi.org/project/psycopg2/) was used to enable python code to execute PostgreSQL commands.
-   [cloudinary:](https://cloudinary.com) was used as database thorughout the project.
-   [Bootstrap:](https://getbootstrap.com) was used for styling.
-   [ILoveImg:](https://www.iloveimg.com) was used for resizing images and editing photos for the website.
-   [Figma:](https://www.figma.com/) was used to create the wireframes during the design process.
-   [Google Fonts:](https://fonts.google.com/) was used to import fonts.
-   [Font Awesome:](https://fontawesome.com/) was used to add icons for aesthetic and UX purposes.


## Testing

### Validating Code
#### HTML & CSS
W3C Markup Validator (https://validator.w3.org/)      
W3C CSS Validator (https://jigsaw.w3.org/css-validator/)

- While these validators effectively assess standard HTML and CSS, they encountered issues comprehending Django's templating language, resulting in reported errors. However, it's important to note that the standard HTML and custom CSS passed validation without errors when processed through these validators.

#### JavaScript
JSHint (https://jshint.com/)

- JavaScript was only sporadically used in this Project but its still worth to note that it gets error free validated by JSHint

#### Python
Pylint (https://pylint.pycqa.org/en/latest/)
Black (https://black.readthedocs.io/en/stable/)

- I integrated Pylint into my project to ensure adherence to the PEP 8 standard. 
- I used Black for autocode formatting to strictly align with PEP 8 guidelines, ensuring consistent and readable code.

The 'Too few public methods' warnings in various classes suggests the potential need for additional methods. However, considering the current functionality of the Classes and Form, its purpose is adequately fulfilled with the existing structure. No further methods are required to enhance their functionality or readability, hence, the warnings can be disregarded.


### Performance

Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 

![Lighthouse Testing](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701694712/lighthouse_testing_1_jdfasw.png)

Lighthouse pointed out that these changes can increase the performance score to maximum rating. In further development of the project, these changes will be worth taking a look at:
- Inlining Critical CSS/JS: Identify critical CSS and JS required for initial rendering. Inline content directly into HTML to allow the browser to render the page without waiting for external resources.

- Deferring Non-Critical Resources: Defer loading non-essential CSS and JS files. This postpones their loading until after the main content has rendered, enhancing the initial load time.

- Asynchronous Loading: Load resources asynchronously wherever possible, especially for non-critical scripts. This allows them to load without blocking the initial page rendering, especially for non-critical scripts. This allows them to load without blocking the initial page rendering.

- Image Compression: Compress images without significantly sacrificing quality. Cloudinary offers various compression techniques to reduce file sizes without visibly impacting image clarity.

- Image Format Optimization: Switching image formats can sometimes significantly reduce file sizes. For instance, converting PNG images to more efficient formats like WebP or JPEG (for photos) might lead to smaller file sizes.

- Specify Image Dimensions: Ensure that the dimensions (width and height) of the displayed images match the actual rendered size. This can prevent unnecessary scaling, reducing file size and load times.

- Lazy Loading: Implement lazy loading for images, loading them only as they come into the viewport. This reduces the initial load time by deferring the loading of off-screen images until they are needed.


### Test Cases and Results

#### Automated Testing
[Heres the Link to the Test Class in my Repo.](https://github.com/ARP-25/TradeConnect/blob/main/tradeboard/test.py)
For this iteration of the App I chose to leave out docstring's for the testcases etc. because the test declarations are very short, descriptive and pregnant. I felt commenting them out largely is massively reducing their readability. However, for future iterations the test's will have to get expanded and I plan to define multiple test files to modulate them and providing docstrings for more complex test's.

Automated Testing completes with zero errors:
![Automated Testing Results](https://res.cloudinary.com/dbui0ebjv/image/upload/v1701696911/automated_testing_results_ta4xew.png)

#### Manual Testing
##### Trade Post List 
| Test Case                          | Expected Outcome                                   | Test Passed |
|------------------------------------|----------------------------------------------------|--------------|
| Load the homepage                  | Displays a paginated list of published trade posts. | &#10004;     |
| Sort by Oldest to Newest           | Posts ordered from the oldest to the newest.        | &#10004;     |
| Sort by Newest to Oldest           | Posts ordered from the newest to the oldest.        | &#10004;     |
| Sort by Highest Rated              | Posts ordered by highest average rating.            | &#10004;     |
| Sort by Lowest Rated               | Posts ordered by lowest average rating.             | &#10004;     |
| Sort by User's Posts (Logged in)   | Shows posts authored by the logged-in user.         | &#10004;     |
| Sort by User's Posts (Not logged)  | No posts displayed when the user is not logged in.  | &#10004;     |

##### Trade Post Detail 
| Test Case                          | Expected Outcome                                                     | Test Passed |
|------------------------------------|----------------------------------------------------------------------|--------------|
| View a TradePost                   | Displays the details of the selected trade post and approved comments.| &#10004;     |
| Add a Comment                      | Successfully adds a comment to the trade post for approval.           | &#10004;     |
| Rate a TradePost                   | Successfully adds a rating to the trade post (once per user).         | &#10004;     |

##### Trade Post Create 
| Test Case                          | Expected Outcome                                           | Test Passed |
|------------------------------------|------------------------------------------------------------|--------------|
| Access TradePost Creation Page     | Shows a form to create a new trade post.                    | &#10004;     |
| Submit TradePost Creation Form     | Successfully creates a new trade post upon form submission. | &#10004;     |

##### Trade Post Edit 
| Test Case                          | Expected Outcome                                        | Test Passed |
|------------------------------------|---------------------------------------------------------|--------------|
| Access TradePost Edit Page         | Displays the selected trade post in an edit form.        | &#10004;     |
| Submit TradePost Edit Form         | Successfully updates the trade post upon form submission.| &#10004;     |

##### Trade Post Delete 
| Test Case                          | Expected Outcome                                      | Test Passed |
|------------------------------------|-------------------------------------------------------|--------------|
| Delete a TradePost                 | Successfully deletes the selected trade post.          | &#10004;     |

##### Contact Message Form 
| Test Case                          | Expected Outcome                                           | Test Passed |
|------------------------------------|------------------------------------------------------------|--------------|
| Submit Contact Form                | Successfully submits a contact message from the form.      | &#10004;     |

##### Login 
| Test Case                          | Expected Outcome                                                      | Test Passed |
|------------------------------------|-----------------------------------------------------------------------|--------------|
| Access Login Page                  | Successfully loads the login page with the username and password form. | &#10004;     |
| Login with Valid Credentials       | Successfully logs in with correct username and password.               | &#10004;     |
| Login with Invalid Credentials     | Properly displays an error message for incorrect username or password. |  &#10004;            |
| Redirect after Successful Login    | Redirects to the expected page after successful login.                  |  &#10004;            |

##### Registration 
| Test Case                          | Expected Outcome                                                           | Test Passed |
|------------------------------------|----------------------------------------------------------------------------|--------------|
| Access Registration Page           | Successfully loads the registration page with the required fields.          | &#10004;     |
| Register with Valid Information    | Successfully creates a new account with valid details.                      |  &#10004;            |
| Register with Existing Username    | Properly displays an error message when attempting to use an existing username. | &#10004;  |
| Verify Email Confirmation          | Receive an email with a verification link and successfully confirm the email. | &#10004;          |
| Redirect after Successful Signup   | Redirects to the expected page after successful registration.               |  &#10004;            |



### Browser Compatibility

- Testing has been carried out on the following browsers :
    - Chrome Version 119.0.6045.200 (Official Build) (64-bit)
    - Firefox Version 120.0.1 (64-Bit)
    - Safari on iPhone (iOS-Version 17.1 (c))



## Deployment

### How this site was deployed



  The live link can be found here - [Tradeconnect](https://tradeconnect-d0f5a2fe7023.herokuapp.com/) 

### How to clone the repository

- Go to the https://arp-25.github.io/tradeconnect/ repository on GitHub.
- Click the "Code" button to the right of the screen, click HTTPs and copy the link there.
- Open a GitBash terminal and navigate to the directory where you want to locate the clone.
- On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process.

## Credits 

### Content 

All the Trade Post data is either fictional or out of my own database.
For styling I tried to imply as much bootstrap as possible, since it was heavily taught in the buildup learning content to pp4.
There was some css integrated for button styling from (https://getcssscan.com/css-buttons-examples).
I also used (https://startbootstrap.com/) and selected a theme as boilerplate to start from.

### Code

Examples and instructions for basic html and CSS code:

- https://developer.mozilla.org
- https://www.w3schools.com
- https://learn.codeinstitute.net/

Additional searching for problemfixes:

- https://stackoverflow.com
- https://www.youtube.com/?gl=DE&hl=de

### Media 
 
- All icons were taken from [Font Awesome](https://fontawesome.com/).
- All fonts used were imported from [Google Fonts](https://fonts.google.com/).


### Shoutout

Special thanks to my Mentor Oluwafemi Medale for helping me out whenever I have a question.