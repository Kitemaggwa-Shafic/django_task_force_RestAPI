# DJANGO TASK FORCE PROJECT (DTF)

## DTF Project Group Assignment for Bootcamp-13
In this project we shall be demostrating to students how to go about Django Installations, Use of some modules in Django eg PostgressSQL, RESTAPi etc to the class
# Pre-Installations
- Create a for your project
- git clone repo
- Install _psycopg2_ using __pip install psycopg2__
- Server configuration
    - configure server _setting_ to your own DB settings.
- Make _python migrations_ for the DB
- Install REST framework module using __pip install      djangorestframewrok__
## Using the REST API
1. This API has two models, course and student
2. Configured locally to run at _http://127.0.0.1:8000_
    - Creating a Course (_http://127.0.0.1:8000/new_course/_)
        - use format __{"courseName":"Python"}__ and POST
    - Adding New Student (_http://127.0.0.1:8000/new_student/_)
    - LIst of all studnets (_http://127.0.0.1:8000/all_students/_)
    - Update Student (_http://127.0.0.1:8000/update_student/id_)
    - Delete Student (_http://127.0.0.1:8000/delete_student/id_)
## Screen shots of API
![Alt text](C:\Users\dell\Pictures\Screenshots\Screenshot (173).png)

## Group Team Members:
1. Oliver Balyama
2. Kitemaggwa Shafic
3. Kamugisha Bruce
4. Dennis Emmanual Ssendagire
5. Kwizera Richard