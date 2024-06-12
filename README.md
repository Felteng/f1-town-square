# F1 Town Square

[Link to live site]() 

## Table of Contents

- [UI/UX](#uiux)
    - [Agile](#agile)
    - [Wireframes](#wireframes)
    - [Site Goals](#site-goals)
    - [5 Planes of UX](#5-planes-of-ux)
    - [Visual Design Choices](#visual-design-choices)
    
- [Features](#features)
    - [Current Features](#current-features)
    - [Future Features](#future-features)
   
- [Database Design](#database-design)
    - [Database Model](#database-model)
    - [Custom Model](#custom-model)
    - [CRUD](#crud)

- [Technologies Used](#technologies-used)
    - [Environemnts](#environments)
    - [Python Libraries and Packages](#python-libraries-and-packages)
    - [Django Packages](#django-packages)
    - [External Libraries and Packages](#external-libraries-and-packages)
    - [Database](#database) 

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Addressed Bugs](#addressed-bugs)
    - [Unaddressed Bugs](#unaddressed-bugs)

- [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Live Deployment](#live-deployment)

- [Source Credits](#source-credits)
    - [Technical](#technical)
    - [Media](#media)
    - [Honorable Mentions](#honorable-mentions)
    

## UI/UX



### Agile



### Wireframes

The initial Balsamiq wireframes are very simplified mockups of site layout to help steer development.


<details>
    <summary>
        Wireframes
    </summary>
    <img src="readme-assets/home-wireframe.png" alt="home-wireframe">
    <img src="readme-assets/articles-wireframe.png" alt="schedule-wireframe">
    <img src="readme-assets/schedule-wireframe.png" alt="schedule-wireframe">
    <img src="readme-assets/mobile-wireframes.png" alt="mobile-wireframes">
</details>

### Site Goals



### 5 Planes of UX

#### Strategy



#### Scope



#### Structure



#### Skeleton



#### Surface



### Visual Design Ideology

**Color Scheme:**
- The base scheme of the site is built with "dark theme" in mind as it's a theme becoming increasingly popular and tends to be a lot easier on the eyes for the user. There is not sacrifice in contrast or user experience to achieve the darker aestetic. The goal is to provide a friendly looking interface that won't appal the user from using the site for any extended period of time.

- To achieve the darker theme every page features shade of woodsmoke as the background. \
![Background color](readme-assets/background-hex.png)

- Furthermore the site incorporates some staple racing colors, such as the very vibrant, scarlet red navigation bar, combined with the white text. \
![Navbar colors](readme-assets/navbar-hex.png)

- Most element borders feature 1 of 2 different shades an olive haze color which aims to provide an organic looking seperation of content. \
![Border colors](readme-assets/border-hex.png)

- The last contrasting color is that of a very dark shade of blue featured at the page footer as well as the hero seperator on an events details page. It blends quite nicely with the dargker background while still providing contrast for content seperation without causing a large shift of focus. \
![Footer color](readme-assets/footer-hex.png)

**Fonts:**
- Racing Sans One
    - The Racing Sans One font has been used in the navbar elements as well as the season calendar heading. Its dynamic and sporty design helps convey a sense of speed, which is the essence of motorsport, and it helps draw attention to the key elements of the site even though they are smaller in size than the ladning page headings. It has very eye catching characteristics yet it remains a very readable font.

- Exo 2
    - Exo 2 has been exerted for all headings on the page bar the calendar heading. It helps convey yet another sense of a modern, sporty feeling albeit while being a lot less robust than the Racing Sans One font. This is perfect because it avoids an overwhelming sense of repetetion in the case that Racing Sans One would be used for all the heading as well as the nav elements, it would very easily split the focus of the user. The sporty modern nature of the font helps the various content headings stand out while not drawing as much attention as Racing Sans One.

- Roboto
    - Roboto features a modern and geometric design with clean lines and a neutral, yet friendly appearance, providing great readability. This makes it the perfect font for the various pieces of content the site aims to convey.

**Images:**
- A wide range of imagery has been used throughout the project to convey a multitude of different meanings.
    - Country flags have been used to represent each event's country. The flags are .svg vectors which is of massive help for scalability and visual consistency across each country's representation. Huge thanks to [lilpis](https://github.com/lipis/flag-icons) for the library used.
    - More .svg vectors have been used for each event to show the layout of the event's track layout. Yet again this provides great scalability and consistency. The creators can be found at [Circuit SVGs](#circuit-svgs).
    - Whenever an event is visited each page features a hero image related to the event in question to help paint a more comprehensive picture of the event as a whole.
    - Lastly another vector is used as the default image if no track layout vector is provided. It is also used for the 3 most recent events visible on the home page to represent the event's finished state.


**Icons:**
- The use of icons have been kept on the lower end and they have simply been used to help convey an elements purpose and action. 2 examples of this is the left caret for the go back button when user lands on a 404 page, and the paper plane icon in the live chat to signify send message. \
    ![Left caret icon](readme-assets/left-caret-ico.png)
    ![Paperplane icon](readme-assets/paperplane-ico.png)


## Features


### Current Features


### Future Features


## Database Design

### Database Model
The entiry relationship diagram for the initial database model was made using [Cacoo's](https://cacoo.com) diagram tool.

![Entity relationship diagram](readme-assets/f1-town-square-erd.png)

### Custom Model


### CRUD

The principles of CRUD are at the essence of this project's features and any future features.

**Create:**
An authenticated user can create comments and send messages in the live chat.

**Read:**
A user can browse and read about the current season's race events and any comments made under them, as well as the conversation in the live chat.

**Update:**
An authenticated user can edit and update their individual contributions to the site.
- The live chat features no database model and the messages are therefore lost whenever the page is refreshed. This is to mimmick the experience of meeting and conversing with a group of individuals with the shared interest of F1 and racing in the real world.

**Delete:**
An authenticated user can delete any of their contributions made to the site.
- The live chat features no database model and the messages are therefore lost whenever the page is refreshed. This is to mimmick the experience of meeting and conversing with a group of individuals with the shared interest of F1 and racing in the real world.

## Technologies Used

### Environments

- [Balsamiq](https://www.balsamiq.com/) (Wireframes)
- [Cacoo](https://cacoo.com/) (ERD creation)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)

### Python Libraries and Packages

- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) (Middleware for efficiently serving static files)
- [psycopg2](https://pypi.org/project/psycopg2/) (Adapter for PostgreSQL databases)

### Django Packages

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [Channels](https://pypi.org/project/channels/) (Augments django with async, and event-driven capabilities- used for the live chat on the home page)
- [Daphne](https://pypi.org/project/daphne/) (Django ASGI (HTTP/WebSocket) server to power Django Channels)
- [django-summernote](https://github.com/summernote/django-summernote) (Embeds Summernote's simple WYSIWYG editor seamlessly into Django- Used for some functional extensions in the admin panel)


### External Libraries and Packages

- [Cloudinary](https://cloudinary.com/) (Hosting and efficient serving of static media files)

### Database

- [CI Database Maker](https://dbs.ci-dbs.net/) (PostgreSQL database hosting provided by Code Institute)

## Testing

### Test Guide


### Validator Testing


#### HTML [W3C validator](https://validator.w3.org/)


#### CSS [Jigsaw](https://jigsaw.w3.org/css-validator/)


#### JavaScript [JSHint](https://jshint.com/) 


#### Python [CI Python Linter](https://pep8ci.herokuapp.com/)


#### Accessibility [axe DevTools Chrome Extension](https://chrome.google.com/webstore/detail/axe-devtools-web-accessib/lhdoppojpmngadmnindnejefpokejbdd)


#### Performance, Accessibility, SEO, Best Practices (Lighthouse Chrome DevTools)


### Browser Testing

**Layout:**


**Functionality:** 


### Addressed Bugs
- Clicking twice in quick succession when confirming the deletion of a comment leads to a 404 error. \
![Delete confirmation](readme-assets/double-click-delete.png)
![Delete confirmation 404 bug](readme-assets/double-delete-404.png)

    - The reason for this is the fact that after the first time the url was called the comment was deleted and the comment with id 41 in the above example no longer exists, so the url cannot be properly built.

        - The solution to the problem was to disable the button from being clicked after the first click with the following line: 
            ```javascript
            $("#confirm-delete").addClass("disabled");
            ``` 
            to this code block:
            ```javascript
            $("#confirm-delete").click(() => {
                $("#confirm-delete").addClass("disabled");
                window.location.href = `delete_comment/${commentId}`;
            });
            ```

- Getting alert of Comment ID not found when confirming deletion. \
![Comment ID not found](readme-assets/comment-id-not-found.png)
    - This occurs because the class that is used to style all the delete buttons was also used on the confirmation button, which is also the class that javascript targets when applying event listeners to all delete buttons.

        - The solution to the problem was to make a seperate class for the confirmation button to keep the same style but not interfere with the javascript:
            ```html
            <button type="button" class="btn delete-btn" id="confirm-delete">Delete</button>
            ```
            to:
            ```html
            <button type="button" class="btn confirm-delete-btn" id="confirm-delete">Delete</button>
            ```
            and in the css file:
            ```css
            .delete-btn {
                background-color: #df2525;
                --bs-btn-hover-bg: #8d1414;
            }
            ```
            to:
            ```css
            .delete-btn, .confirm-delete-btn {
                background-color: #df2525;
                --bs-btn-hover-bg: #8d1414;
            }
            ```

- Cannot read properties of null live chat input. \
![Console error](readme-assets/cannot-read-prop.png)
    - This console error is logged whenever an unauthenticated user visits the homepage, when the live chat message input is attempted to be put into focus.

        - The solution to this issue was to check whether or not the input field is visible (Which it only is to a logged in user) and then add the call focus():
        ```javascript
        document.querySelector("#id_message_send_input").focus();
        ```
        to:
        ```javascript
        if (document.querySelector("#id_message_send_input")) {
            document.querySelector("#id_message_send_input").focus();
        }
        ```

- Mobile user gets scrolled to the bottom of the homepage when visiting.

    - Whenever a logged in user visits from a device with a width smaller than 768px, essentially using the 1 column layout, they are scrolled down to the bottom of the page where the live chat input field is located. The reason this occurs is because the input field is put into focus when loaded.

        - To solve this this code was modified:
        ```javascript
        if (document.querySelector("#id_message_send_input")) {
            document.querySelector("#id_message_send_input").focus();
        }
        ```
        to:
        ```javascript
        if (document.querySelector("#id_message_send_input")) {
            if (window.matchMedia("(min-width: 768px)").matches) {
                document.querySelector("#id_message_send_input").focus();
            }
        }
        ```


### Unaddressed Bugs


## Deployment

### Local Deployment


### Live Deployment


## Credits

### Technical
- [caffsushi](https://stackoverflow.com/a/57682143) - For forcing https protocol over http when loading images from cloudinary by accessing an objects .url tag.
- [dgel](https://stackoverflow.com/a/12003808) - Decorator for checking if a user has superuser status in views.

### Media
#### Circuit SVGs
- By ごひょううべこ - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=116112303
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=131259613
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=130609950
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=123016102
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=117733185
- By Will Pittenger - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=7874957
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=117068808
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=118372959
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=132472444
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=119373063
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=120207427
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=119963852
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=121215630
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=122326833
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=122553324
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=122791737
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=131260604
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=122949767
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=124173727
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=124590600
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=125242034
- By Valentin JJ. - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=127545359
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=132507300
- By ごひょううべこ - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=125647671




#### Hero images
- CaterhamF1, https://www.flickr.com/photos/caterhamf1/13678967474
- Automotive Rhythms, https://www.flickr.com/photos/artvlive/51696022965
- By Chris Phutully - https://www.flickr.com/photos/72562013@N06/13186495033/, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=31802460
- By Norimasa Hayashida - https://www.flickr.com/photos/nhayashida/10347531595/in/set-72157636691519286, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=29868692
- By Derrick Noh from NYC - 2009 Formula 1 Grand Prix of China - Shanghai Circuit, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=60429722
- By Bassfish22 - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=136303048
- By Wastrick - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=121017386
- By pedrik - First corner, GP of Canada 2017, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=128994359
- By Anyul Rivas - https://www.flickr.com/photos/anyulled/42253655511/, CC BY 2.0, https://commons.wikimedia.org/w/index.php?curid=107128061


- By Santiago Puig Vilado…, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=52434602

- By chensiyuan - chensiyuan, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=21856333

#### Favicon
- Site favicon from [Favicon.io](https://favicon.io)

### Honorable Mentions
