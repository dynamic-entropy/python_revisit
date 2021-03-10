import grpc
from flask import Flask, render_template

from client.client import rclient

app = Flask(__name__)


@app.route("/")
def render_homepage():
    print("Markeplace Starting ... ")
    response = rclient()
    return render_template("index.html", recommendations=response)
