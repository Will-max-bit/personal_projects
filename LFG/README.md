# LFG

repo for LFG project


## Overview
------
LFG will be a social network for gamers, it will have a main page with all posts, a my games page with posts related to games the user follows and a user profile.

### Technologies used

* Django 3.1
* VueJS 3.0
* Bootstrap v5.0

## Features 
----

- User System
    -Login/logout
    -create profile
- Post
    -CRUD
    -Like
    -comment
- Games
    -following games
- Following
    -following users
    -followers

## Data Model
* Game
    * name(charfield)
* Post
  * title (charfield)
  * text (textfield)
  * game (foreignkey to Game)
  * author (foreignkey to User)
  * post_image(imagefield)
  * created_date (datetimefield)
  * likes(manytomany to user)
* Userfollowing
    *userid(foreign key to the user)
* User
    * user(onetoOneField)
    * image(imagefield)

## pages
-Index
    -main page posts
    -likes on posts
    -navbar with selectable links reloading page with different data
    -online now users of follwing users
    -updates by following users, showing their posts.
-Post detail
    -should display comments along with post data
-Profile page
    -display users posts
    -display comments by user
    -profile image of user at the top
    -favorite games 
    -a follow button
-Registration page
    -register user w/name, picture and other info like games etc
    -log the user in
-Log in page
    -check the user against the database
    -display messages depending on success or failure
