from flask import Flask, jsonify, request

# Initialise the app
app = Flask(__name__)


# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """
    # return "Hello, World!"

    # response = {"data": "Hello, World!"}
    # return jsonify(response)

    # name = request.args.get("name")
    #  if not name:
    #     return jsonify({"status": "error"})
    # response = {"data": f"Hello, {name}!"}
    # return jsonify(response)

    fname = request.args.get("fname")
    lname = request.args.get("lname")

    #   if neither provided
    if not fname and not lname:
        return jsonify({"status": "error"})

    # only first name provided
    elif fname and not lname:
        response = {"data": f"Hello, {fname}!"}

    # only last name provided
    elif not fname and lname:
        response = {"data": f"Hello, Ms. {lname}!"}

    # both first and last name provided
    else:
        response = {"data": f"Your name is {fname} {lname}!"}

    return jsonify(response)