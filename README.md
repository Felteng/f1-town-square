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

**Colour Scheme:**


**Fonts:**


**Images:**


**Icons:**


## Features


### Current Features


### Future Features


## Database Design

### Database Model
The entiry relationship diagram for the initial database model was made using [Cacoo's](https://cacoo.com) diagram tool.

![Entity relationship diagram](readme-assets/initial-erd.png)

### Custom Model


### CRUD

The principles of CRUD are at the essence of this project's features and any future features.

**Create:**
An authenticated user can create comments and send messages in the live chat.

**Read:**
A user can browse and read about the current season's race events and any comments made under them, as well as the conversation in the live chat.

**Update:**
An authenticated user can edit and update their individual contributions to the site.

**Delete:**
An authenticated user can delete any of their contributions made to the site.

## Technologies Used

### Environments

- [Balsamiq](https://www.balsamiq.com/) (Wireframes)
- [Cacoo](https://cacoo.com/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)

### Python Libraries and Packages


### Django Packages

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)
- [Channels](https://pypi.org/project/channels/) (Augments django with async, and event-driven capabilities- used for the live chat on the home page)
- [Daphne](https://pypi.org/project/daphne/) (Django ASGI (HTTP/WebSocket) server)

### External Libraries and Packages


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
- Clicking twice in quick succession when confirming the deletion of a comment leads to a 404 error.
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

- Getting alert of Comment ID not found when confirming deletion,
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

- Cannot read properties of null live chat input.
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

By Santiago Puig Vilado…, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=52434602

- By chensiyuan - chensiyuan, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=21856333

#### Favicon
- Site favicon from [Favicon.io](https://favicon.io)

### Honorable Mentions
