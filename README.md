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
