from flask import Blueprint, render_template

crud = Blueprint('crud', __name__)

#landing page
@crud.route("/home")
def home():
    return render_template("home.html")

