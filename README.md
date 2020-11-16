# MVC View Controller

**Display data on the browser using HTML, CSS, JS, and Bootstrap**

- HTML - Hyper Text Markup Language 
- CSS - Cascading Style Sheet
- JS - JavaScript
- BOOTSTRAP

**Building our APIs**
- display data from python flask to specific API call/url/end-point

**Flask**
- Flask is a web app framework 
- Very powerful to interact with DB and user interface/browsers etc
- Flask can be used to create an API
- Allows us to integrate with HTML. CSS etc
- Allows us to map HTTP requests to python functions - URL - HTTP GET
- Allows us to set the API path as URL to view in the browser

**Steps**
- install flask using: ```pip install flask```
- Run the flask app using ```flask run```
- create an instance of the app:
```python
app = Flask(__name__)
```
- Use a decorator to create our api/url for user to access data in the browser:
```python
@app.route("/") # localhost:5000 is the default port for flask
```
- create a function that returns the content of the webpage
```python
def home():
    return "<h1>Consultant team</h1>
```
- This function runs when the API/URL is accessed
- you can add html code because it gets integrated by flask
- run the flask app and click on the url: http://127.0.0.1:5000/ 
- the webpage will display the data specified in the home() function
- you can use jsonify to transform data into json
```python
from flask import Flask, jsonify

students = [
    {
        "id": 0,
        "title": "Mr.",
        "firstname": "Ubaid_ur-rehman",
        "lastname": "Muhammad",
        "course": "DevOps"
    }
]

# creating our own API to display data on the specific route/url/end-point
@app.route("/api/v1/student/data", methods=["GET"])
# this will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # transforms data into json
    # Using Extract Transform Load
```
- you can redirect to another url by importing redirect and url_for
```python
@app.route("/welcome/")
def greet_user():
    return "Welcome to DevOps"

@app.route("/login/")
def login():
    return redirect(url_for("greet_user"))
```
- going on the login page will redirect user to the welcome page

**Interacting with HTML**
- Naming conventions are essential
- We need to create a templates folder in our directory
- flask looks for templates folder and anything inside that folder
- we will create index.html inside the templates folder