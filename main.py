from flask import Flask, render_template, request, redirect
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID

import db

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")
app.config.update(dict(
    DEBUG=True
))


@app.route('/')
def home():
    print(db.User.get(email="asd@example.com").data)
    return render_template("index.html")


# ToDo: Passwords need hashing
# ToDo: OpenID
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = db.User.get(**request.form)
        if user:
            return "Login successful!<br>Welcome {}".format(user.data["username"])
        else:
            return "Invalid username/email or password."
    else:
        return render_template("forms/login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db.User.new(request.form["username"], request.form["password"], request.form["email"])
        return str(db.User.get(email=request.form["email"]))
    else:
        return render_template("forms/register.html")

if __name__ == '__main__':
    app.run()
