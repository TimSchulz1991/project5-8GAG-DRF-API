# 8GAG - [Live link](https://drf-api-8gag.herokuapp.com/)

If you want to laugh and enjoy some good memes, you have come to the right place - to 8GAG!

This repository contains information about the Django REST Framework API, built specifically for the 8GAG frontend React application ([Repo here](#) and [deployed website here](#)).

All the information about the project, its goals, the end user stories, and much more can be found in the [README]() of the frontend 8GAG application.

# Data Model

The backend API for the 8GAG project was built with the Django REST Framework.

## ERD

Below you can see the ER diagram for this project, to get an instant overview of the different models used. 

![This image provides an overview of the database models](media/readme/ERD_project5.png)

### User model

- id of the User model is linked via a OneToOne relation to the Profile model owner field
- id of the User model is linked via a ForeignKey relation to the Post model owner field
- id of the User model is linked via a ForeignKey relation to the Comment model owner field
- id of the User model is linked via a ForeignKey relation to the Like model owner field

### Post model

- id of the Post model is linked via a ForeignKey relation to the Comment model post field
- id of the Post model is linked via a ForeignKey relation to the Like model post field

## Database

- SQLite was used in delevopment to store data
- PostgreSQL is used in production to store data

# User Stories

For the backend part of this entire 8GAG project, there is only one user story: 

- As an admin, I want to be able to manage all the users, posts, comments and likes, so that I can for example delete malicious content from the page

# Agile

For this project the GitHub Kanban agile project management tool was used to create EPICs, add User Stories to these EPICs --> [8GAG Kanban](https://github.com/TimSchulz1991/project5-8GAG-React/projects/1). 

Throughout the development process, the stories were constantly updated according to the progress and pushed into the right cloumn (in progress / done).
![This image provides an overview of the Kanban board on Github](media/readme/kanban-api.png)

# Technologies

## Languages used
- [Python](https://www.python.org/)

## Workspace

### Gitpod
[GitPod](https://gitpod.io/) was used as a virtual IDE workspace to build this site.

## Version Control

### Git
[Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to add and commit to Git and push to GitHub.

### GitHub
[GitHub](https://github.com/) is used to store the code for this project after being pushed from Git.

## ERD

### Lucid
[Lucid](https://lucid.app/) was used to create the ERD overview.

## Development

### Django Rest Framework
[Django REST Framework](https://www.django-rest-framework.org/) was used to build the backend API.

### Django AllAuth
[Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html) was user for user authentication.

## Hosting/Database

### Heroku
[Heroku](https://id.heroku.com/login) is used to host the application.

### Gunicorn
[Gunicorn](https://gunicorn.org/) is used for deploying the project to Heroku.

### Cloudinary
[Cloudinary](https://cloudinary.com/) is used to host the static and media files and serve them to Heroku.

### Pillow 
[Pillow](https://pillow.readthedocs.io/en/stable/) was used for image processing and validation.

### Psycopg2
[psycopg2](https://www.psycopg.org/docs/) was used for PostgreSQL Python adaption.

### PostgreSQL
[PostgreSQL](https://www.postgresql.org/) is used as the production database.

# Testing

## Pep8

- [PEP8](http://pep8online.com/) shows no errors, except for some default lines being too long in the settings.py file.

## Manual testing of user stories

Relating back to the user story of this README: 
- As an admin, I want to be able to manage all the users, posts, comments and likes, so that I can for example delete malicious content from the page
    - All works as intended. The testing is described in more detail in the table below.

