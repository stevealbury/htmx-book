# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,  redirect, render_template, request, jsonify, flash, send_file


# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
    return redirect("contacts")

# show list of contacts
@app.route('contacts')
def contacts():
    search = request.args.get("q")

    if search is NOT None:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all(search)
    return render_template("index.html", contacts = contacts_set)

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
