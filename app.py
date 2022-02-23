from collections import namedtuple
from flask import Flask, request, render_template
from forms import EmailPasswordForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

User = namedtuple("User", field_names=["email_login", "password"])
user = User(email_login="john@black.com", password="black")

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            if form.email_login.data == user.email_login and form.password.data == user.password:
                print("you are logged")
                return "you are logged"
            else:
                print(" złe hasło ")
                return "złe pasy"
        else:
            error = form.errors
    return render_template("/email_login.html/", form=form, error=error)