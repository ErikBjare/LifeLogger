from flask import Flask, render_template
app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.update(dict(
    DEBUG=True
))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return "Nothing to see here, yet"

if __name__ == '__main__':
    app.run()
