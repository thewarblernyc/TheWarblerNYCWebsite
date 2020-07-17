from flask import Flask, render_template
# initialize flask "app" (that's what the documentations call it :/) 
app = Flask(__name__)

@app.route("/")
def index():
    """Homepage for the Warbler Org."""
    return render_template("index.html")

@app.route("/resource")
def resource():
    """Resources page for the Warbler Org."""
    return render_template("resource.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")