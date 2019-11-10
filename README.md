# BiblioBin
### Who doesn't love books?
BiblioBin is a book review web app developed using Flask and SQL. 
You can search for books, leave reviews for individual books, and see the reviews made by other people.

# Getting Started
## PostgreSQL
For this project, you’ll need to set up a PostgreSQL database to use with our application. It’s possible to set up PostgreSQL locally on your own computer, but for this project, we’ll use a database hosted by Heroku, an online web hosting service.

* Navigate to https://www.heroku.com/, and create an account if you don’t already have one.
* On Heroku’s Dashboard, click “New” and choose “Create new app.”
* Give your app a name, and click “Create app.”
* On your app’s “Overview” page, click the “Configure Add-ons” button.
* In the “Add-ons” section of the page, type in and select “Heroku Postgres.”
* Choose the “Hobby Dev - Free” plan, which will give you access to a free PostgreSQL database that will support up to 10,000 rows of data. Click “Provision.”
* Now, click the “Heroku Postgres :: Database” link.
* You should now be on your database’s overview page. Click on “Settings”, and then “View Credentials.” This is the information you’ll need to log into your database. You can access the database via Adminer, filling in the server (the “Host” in the credentials list), your username (the “User”), your password, and the name of the database, all of which you can find on the Heroku credentials page.
* Alternatively, if you install PostgreSQL on your own computer, you should be able to run psql URI on the command line, where the URI is the link provided in the Heroku credentials list.

# Python and Flask
First, make sure you install a copy of Python. For this course, you should be using Python version 3.6 or higher.
You’ll also need to install pip. If you downloaded Python from Python’s website, you likely already have pip installed (you can check by running pip in a terminal window). If you don’t have it installed, be sure to install it before moving on!
To try running your first Flask application:

* Download the project1 distribution directory from https://cdn.cs50.net/web/2019/x/projects/1/project1.zip and unzip it.
* In a terminal window, navigate into your project1 directory.
* Run pip3 install -r requirements.txt in your terminal window to make sure that all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.
* Set the environment variable FLASK_APP to be application.py. On a Mac or on Linux, the command to do this is export FLASK_APP=application.py. On Windows, the command is instead set FLASK_APP=application.py. You may optionally want to set the environment variable FLASK_DEBUG to 1, which will activate Flask’s debugger and will automatically reload your web application whenever you save a change to a file.
* Set the environment variable DATABASE_URL to be the URI of your database, which you should be able to see from the credentials page on Heroku.
* Run flask run to start up your Flask application.
* If you navigate to the URL provided by flask, you should see the text "Project 1: TODO"!

# Goodreads API
Goodreads is a popular book review website, and we’ll be using their API in this project to get access to their review data for individual books.

* Go to https://www.goodreads.com/api and sign up for a Goodreads account if you don’t already have one.
Navigate to https://www.goodreads.com/api/keys and apply for an API key. For “Application name” and “Company name” feel free to just write “project1,” and no need to include an application URL, callback URL, or support URL.
* You should then see your API key. (For this project, we’ll care only about the “key”, not the “secret”.)
* You can now use that API key to make requests to the Goodreads API, documented here. In particular, Python code like the below
~~~python
import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "KEY", "isbns": "9781632168146"})
print(res.json())
~~
