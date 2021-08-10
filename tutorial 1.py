//Python

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", content=["tim","joe","bill"])
 

if __name__ == "__main__":
    app.run() 
    
    
 --html

<!doctype html>
<html>
    <head>
        <title>Home page</title>
        </head>
        <body>
            <h1>Home Page!</h1>
          {% for x in range(10) %}
          {% if x % 2 == 1 %}
            <p>{{x}}</p>
            {% endif %}
            {% endfor %}
        </body>
    </html>
