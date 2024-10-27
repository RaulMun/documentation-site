from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

#this block of code must include the following:
@auth.route('/login') #the route that will be shown in the link
def login(): #define of the page, standard to call it the same as the page name
    return render_template("login.html") #render_template to render the html with that name in templates

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("signup.html")
