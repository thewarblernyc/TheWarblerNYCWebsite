from flask import Flask, render_template
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


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
    """Contacts page for the Warbler Org."""
    return render_template("contact.html")


@app.route("/about")
def about():
    """About page for the Warbler Org."""
    return render_template("about.html")

# app.run(host='0.0.0.0')
