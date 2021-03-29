# landing page
Repo for personal landing page

## overview 

landing page will be blog style web application where I post daily programming updates, things I've learned, pictures of code and other general programming related endeavours 

### Technologies Used

* Django 3.1
* VueJS 3.0
* Bootstrap V5


## Features

    -SPA
    -New post form
    - Post sorted by created date
    - Sort by type, Code challenge, new project update etc


## Data Model
-------
* Post
    * title (charfield)
    * text (textfield)
    * post_image(imagefield)
    * created_date (datetimefield)
    * category (foreign key to Category)
* Category
    * name(charfield)

## Page
-------
- Index
    - new post
    - list of posts
    - navbar sticky
    - sort button w/dropdown list

## Schedule
* Week 1
    * create models
    * create template
    * Show test posts
    * implement sorting UI

* Week 2
    * style page
    * fix any issues
    * add new features as they come
* Week 3 
    * deploy and host webpage
