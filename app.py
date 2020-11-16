from flask import Flask

# create an instance of our app
app = Flask(__name__)

students = [
    {
        "id": 0,
        "title": "Mr.",
        "firstname": "Ubaid_ur-rehman",
        "lastname": "Muhammad",
        "course": "DevOps"
    }
]

# decorator - to create our api/url for user to access our data in the browser
@app.route("/") # localhost:5000 is the default port for flask
def home():
    return "Consultant team"
# This function runs when the API/URL is accessed

if __name__ == "__main__":
    app.run(debug=True)


