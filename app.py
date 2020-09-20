from flask import Flask, render_template
import json

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
publications = json.load("data/publication.json")

@app.route("/")
def home():
    """Homepage for the Warbler Org."""
    return render_template("index.html")


@app.route("/publication")
def resource():
    """Publications page for the Warbler Org."""
    return render_template("publication.html")


@app.route("/contact")
def contact():
    """Contacts page for the Warbler Org."""
    return render_template("contact.html")


@app.route("/about")
def about():
    """About page for the Warbler Org."""
    return render_template("about.html")

# app.run(host='0.0.0.0')