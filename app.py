from collections import namedtuple
from flask import Flask, request, render_template
from forms import EmailPasswordForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

User = namedtuple("User", field_names=["email_log", "password"])
user = User(email_log="john@black.com", password="black")

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            if form.email_log.data == user.email_log and form.password.data == user.password:
                return "You are logged id"
            else:
                return "Wrong credentials!!"
        else:
            error = form.errors
    return render_template("/email_login.html/", form=form, error=error)