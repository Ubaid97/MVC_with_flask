from flask import Flask, jsonify

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
    return "<h1>Consultant team</h1>"
# This function runs when the API/URL is accessed

if __name__ == "__main__":
    app.run(debug=True)


# creating our own API to display data on the specific route/url/end-point
@app.route("/api/v1/student/data", methods=["GET"])
# this will add this API/URL to http://127.0.0.1:5000/api/v1/student/data
def customised_api():
    return jsonify(students) # transforms data into json
    # Using Extract Transform Load