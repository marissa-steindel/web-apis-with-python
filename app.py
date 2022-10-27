# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    # Since this is a website with front-end, we don't need to send the usage instructions
    response = {"usage": "/dict?=<word>"}
    return jsonify(response)


@app.get("/dict")
def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    word = request.args.get("word")

    if not word:
        return jsonify({"data": "Not a valid word or no word provided"})

    definitions = match_exact(word)
    if definitions:
        return jsonify({"data": definitions})

    definitions = match_like(word)
    if definitions:
        return jsonify({"data": definitions})
    else:
        return jsonify({"data": "word not found"})



if __name__ == "__main__":
    app.run()
