from datetime import date, timedelta
import calendar
from random import randint
import pprint

from flask import Flask, render_template, request

import db


app = Flask(__name__, static_folder="web/static", template_folder="web/templates")
app.config.update(dict(
    DEBUG=True
))


@app.route('/')
def home():
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


@app.route('/sheet', methods=['GET'])
def view_sheet():
    # Testing constants
    start_date = date(2014, 3, 1)
    day = timedelta(days=1)

    user_erb = db.User.new(username="erb", email="erik.bjareholt@gmail.com", password="testing")
    sheet = db.Sheet.new(user_erb)

    # Try to build sheet if not built
    try:
        sheet.add_3_a_day("mood")
        sheet.add_3_a_day("productivity")
        sheet.add_group("exercise")
        sheet.add_field("gym", "exercise")
        sheet.add_field("running", "exercise")
        sheet.add_field("biking", "exercise")

    except KeyError:
        pass

    rows = []

    for i in range(calendar.monthrange(sheet.data["year"], sheet.data["month"])[1]):
        cells = []
        for group, labels in sheet.data["order"]:
            first = True
            for _ in labels:
                border_style = "border-left: black solid 1px;" if first else ""
                first = False
                val = randint(1, 10)
                color = "red" if val < 3 else ("yellow" if val < 7 else "green")
                cells.append("<td class=\"{}\" style=\"{}\">{}</td>".format(color, border_style, val))
        row_date = str((start_date+i*day).isoformat())
        rows.append((row_date, cells))

    sheet_pretty = pprint.pformat(sheet.data)

    return render_template('sheet.html', rows=rows, sheet=sheet, sheet_pretty=sheet_pretty, user=user_erb)

if __name__ == '__main__':
    app.run()
