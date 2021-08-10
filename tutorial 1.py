//Python-- tutorial 3.py

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content="Testing")
 

if __name__ == "__main__":
    app.run(debug=True) 
    
    
 --index.html
{% extends "base.html" %}
{% block title %}Home Page{% endblock %}
{% block contet %}
<h>Test</h>
{% endblock %} 

    
 --base.html

<!doctype html>
<html>
    <head>
        <title>{% block title %}{% endblock %}</title>
        </head>
        <body>
            <h1>Tim's.Website</h1>
            {% block content %}
            {% endblock %}
        </body>
    </html>

