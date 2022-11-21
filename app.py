from flask import Flask, redirect, url_for, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy

from datetime import timedelta
#API, login, images, links

app = Flask(__name__)
app.secret_key = "123"
app.permanent_session_lifetime = timedelta(minutes=5)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash(f"You have logged in, {user}", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash(f"Already logged in!", "info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Email was saved", "info")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have logged out, {user}", "info")
        session.pop("user", None)
        session.pop("email", None)
    return redirect(url_for("login"))


"""
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    #url_for takes function name and any arguments as variables
    return redirect(url_for("user", name="Bart"))
"""

if __name__ == "__main__":
    app.run(debug=True)