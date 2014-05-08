from flask import Flask, render_template, request, redirect

import db

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")
app.config.update(dict(
    DEBUG=True
))


@app.route('/')
def home():
    print(db.User.get(email="asd@example.com").data)
    return render_template("index.html")


@app.route('/login')
def login():
    return "Nothing to see here, yet"


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        db.User.new(request.form["username"], request.form["password"], request.form["email"])
        return str(db.User.get(email=request.form["email"]))
    else:
        return render_template("register.html")

if __name__ == '__main__':
    app.run()
