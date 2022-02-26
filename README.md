# LITReview

LIReview is a site that allows you to consult or create reviews on books or to request reviews on a particular book by creating a ticket.

It also allows you to follow users.

__It allows to :__

- Create account
- Create tickets (book review request).
- Create reviews (in response to a ticket or not).
- Subscribe to users and vice versa.
- View their ticket and review posts.
- Consult a feed where will appear :
  - Our own publications.
  - The answers to our tickets
  - Tickets and reviews of followed users.

<li><a href="#requirements">Requirements</a></li>
<li><a href="#gitbash">Gitbash</a></li>
<li><a href="#installation-on-windows">Installation on Windows</a></li>
<li><a href="#installation-on-linux">Installation on Linux</a></li>
<li><a href="#installation-on-mac">Installation on Mac</a></li>
<li><a href="#site-management">Site Management</a></li>


## Requirements
```bash
Python 3.9.0
```
## Gitbash
You have to clone the deposit with this command on gitbash :
```
git clone https://github.com/Papiex/LITReview-Web-Application
```

## Installation on Windows
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
- if you use PowerShell :
``` env/Scripts/activate.ps1```
- if you use CMD or terminal that supports __.bat__ :
``` env/Scripts/activate.bat```

## Installation on Linux
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Installation on Mac
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Libraries
__This program need some libraries, for installing them, use this command (in your virtual env) :__

*View requirements.txt to know which library/version is used*

- ```pip3 install -r requirements.txt``` | Windows : ```pip install -r requirements.txt```

## Run the site
__To run the site, after activating your virtual environment
You need to start the server with this commands :__

- ```cd litreview```
- ```python3 manage.py runserver``` | Windows : ```python manage.py runserver```
- Open your browser and go to this url : 127.0.0.1:8000


## Site management

### Create superuser
__To manage the site, you must create a super user account by following these steps :__
- At the root of the project 'LITReview-Web-Application/litreview/'
Run this command :
<br></br>
-```python3 manage.py createsuperuser``` | Windows : ```python manage.py createsuperuser```
- Choose a username
- Enter your mail
- Enter your password twice

![image](https://user-images.githubusercontent.com/81369778/152770521-eba4163a-fbc0-4889-a2bd-e3a6544cc391.png)


Launch the server with this command :
<br></br>
- ```python3 manage.py runserver``` | Windows : ```python3 manage.py runserver```
- Open your browser and go to this url : 127.0.0.1:8000/admin/
- Connect with your identifiers previously created.

### Managment Administration Panel

<li><a href="#manage-users">Manage Users</a></li>
<li><a href="#manage-tickets">Manage Tickets</a></li>
<li><a href="#manage-reviews">Manage Reviews</a></li>
<li><a href="#manage-userfollows">Manage UserFollows</a></li>

<br></br>

![image](https://user-images.githubusercontent.com/81369778/154242862-aa459878-3c68-403f-bae2-99f309787ae8.png)

### Manage Users

- In this tab, you can add users or modify existing ones :

![image](https://user-images.githubusercontent.com/81369778/154245543-7269a607-6f9d-474b-9808-f901a598f8c6.png)

### Manage Tickets

- In this tab, you can add tickets or modify existing ones :

![image](https://user-images.githubusercontent.com/81369778/154245964-33bc208b-c6ef-43ef-9123-eaf7ccbbe399.png)

![image](https://user-images.githubusercontent.com/81369778/154246205-cfff2b89-4dea-4cfa-94c7-00d89aa45d7d.png)

Before saving it, you will have to complete the fields ( Fields in bolds are required )
 - __is_processed__ corresponds to the review in response to the ticket, it allows you to know if a ticket has already been answered
 - __is_archived__ corresponds to the deletion of the ticket, it will not be deleted but archived so it will not be visible.
 
 _If a ticket is deleted, the corresponding review (if there is one) will be automatically archived_

### Manage Reviews

- In this tab, you can add reviews or modify existing ones :

![image](https://user-images.githubusercontent.com/81369778/154248008-2acf4c79-6252-4938-ad35-d83c27e9e3a5.png)

![image](https://user-images.githubusercontent.com/81369778/154248172-c22e881b-a068-44d7-b812-5976eab8edb2.png)

Before saving it, you will have to complete the fields ( Fields in bolds are required )

You must select an existing ticket, or you can create one by clicking the green button on the right.

### Manage UserFollows

- In this tab, you can see user associations. You have the user on the left and the followed user on the right.

![image](https://user-images.githubusercontent.com/81369778/154249347-203f92be-51e1-488a-a851-c53a5af78fa1.png)

![image](https://user-images.githubusercontent.com/81369778/154250049-df959f23-eadd-4c36-a28d-d57e04d688e9.png)

You can add or modify user associations.
