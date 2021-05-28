# Send it
----
## Overview
a social media app centered around routes at gyms, they're ratings, how many have completed it, type of route, setter.

### Features
- User System
    - [ ]login/logout
    - [ ]update profile
    - [ ]delete profile
- profile page
    - [ ]profile picture
    - [ ]recent activity
    - [ ]historical activities,
- posts 
     - [ ]photo and maybe video only no text based
- gym pages
    - [ ]setters at gym
    - [ ]current routes
    - [ ]gym information
- home page
    - [ ]featuring followed setters, gyms, users
- discover feed
    - [ ]featuring posts by users and gyms dependent on interests

## Data Model
* User (extends built in user model)
    * is_climber(boolean field)
    * is_setter(boolean field)
    * is_gym(boolean field)
* Userfollowing
    * user(foreign key to the user)
    * following( foreign key to user)
* Post
    * post_image(imagefield)
    * author (foreign key to the user)
    * likes( many to many field)
    * title( charfield)
    * created date (datetimefield)
* Rating 
    * rating(charfield)
    * type(charfield)
* Comments
    * post(foreign key to post)
    * author(foreign key to user)
    * body(text field)
    * created on(date time field)
    * active( booleanfield)

## Pages
- Index
  - greeting
  - list of posts by followed accounts
    - likes on post
    - completions
    - type
    - comments on posts
    - 

  - button for creating a new post
    - route completed shared from the gym/setters post
    - video or image of user on route or route itself.
  - header
    - link to profile page
    - log-in link if not logged in
    - log-out link if logged in
- Registration
    - user registration form using django forms
    - imagefield for profile picture
- Login
  - login form
  - welcome message displaying on main page after redirect
- Profile page
  - display users posts chronologically
  - fixed navbar at bottom displaying current page and current user

