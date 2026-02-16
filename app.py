import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hello.html")

# Déposez votre code à partir d'ici :

@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"



# Ne rien mettre après ce commentaire
