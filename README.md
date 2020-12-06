# Data Representation

# **Web Application Project**

The following project contains:
    1. A Flask server that has a REST API (performing the CRUD operations)
    2. An SQL database
    3. Web interface, that uses AJAX calls to perform the CRUD operations


For more information please visit the Githib repository: 
https://github.com/JuliaMal/dataRep_Pythonanywhere

The link to the project running on PythonAnywhere:
http://julitocka.pythonanywhere.com/memberviewer.html

The Github repository contains the following files:
   1. application.py - FLASK server
   2. memberDAO.py - REST API
   3. memberviewer.html - web interface of the GYM Members
   4. Requirements.txt - list of libraries that need to be installed on a virtual enviroment
   5. css-styles.css - file that contains css styles for the web page
   6. background.jpg - background picture
   7. SQL_table - description of the SQL table
   8. dbconfig.py - contains the information about host, user, password and database 
   9. ReadMe.md - This is a Markdown file, containing explanation what is saved in the Github repository and instructions how to run the project.
   10. .gitignore - This file tells git which files (or patterns) should be ignored. In our case it's Python and virtual enviroment - venv.

How to run the web application:

    - The Web application is hosted online using PythonAnywhere
    - Just click on the link: http://julitocka.pythonanywhere.com/memberviewer.html to be redirected to the Gym Members database
    - By default you will get the list of all gym members, currently maintained in the mySQL DB
    - If you want to add a new member, press the button Create on the top left corner on the page
    - If you want to change the info about a particular member, choose the member and click the button Update
    - If you want to delete a member from the database, choose the member and click Delete. This will permamently remove the member's data from the DB.
