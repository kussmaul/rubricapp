@ -1,60 +1,17 @@

# RubricApp

set up Selenium, make sure browsers driver is on path

RubricApp is a web application for evaluating students' professional skills, such as teamwork and communication. With RubricApp, instructors can assess teams of students in real-time using [research-based rubrics](http://elipss.com/) or custom rubrics. Instructors can email students their results, as well as download the data for analysis. RubricApp is the software behind ELIPSS SkillBuilder.
requires packages

## Install requirements

unittest
selenium
nose

Requires python 3.

To install required python packages, either:
run all tests with
make sure server is running
nosetests

a) pip install -r requirements.txt

OR

b) Using the method of your choice, individually install each of the python packages listed in requirements.txt.

To install webdriver_manager

pip3 install webdriver_manager

Webdriver Manager ensures your webdriver PATH is correct

## Running the application

### With Flask's test web server

From the base directory...

Before running the application for the first time, you need to create the database.

```
python dbcreate.py `pwd`
```

To run the test server.

```
python app.py `pwd`
```

The command will print out some logging information, including a localhost URL (probably http://127.0.0.1:5000/). Go there in your web browser to see the site.

### Chromedriver

Ensure the version of Chromedriver downloaded to your machine matches the version of Chrome currently installed on your machine

#### Using a different location for the database

If for some reason you want the sqlite database file and users directory to live somewhere else, replace \`pwd\` in the above commands with the desired path. Just make sure that the paths for both commands are the same.

### With Apache

The application can run in Apache. Look up information about running WSGI apps in Apache.

# Contact

RubricApp is developed at the University of Iowa.

- For development questions or trying our test server: [brandon-d-myers@uiowa.edu](mailto:brandon-d-myers@uiowa.edu)
- For information about the rubrics: http://elipss.com/
  see

* https://www.selenium.dev/documentation/en
* best practices at https://www.selenium.dev/documentation/en/guidelines_and_recommendations/
