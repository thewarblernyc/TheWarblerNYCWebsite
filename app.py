from flask import Flask, render_template, request, redirect
import psycopg2
import os
import mammoth
import json

# configure flask app
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect to Heroku Postgres Database
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

# Load json file containing publication data
with open('data/publication.json') as F:
    publications_data = json.load(F)["publications"]


@app.route("/")
def home():
    """Homepage for the Warbler Org."""
    return render_template("index.html")


@app.route("/publications")
def showPublications():
    """Publications page for the Warbler Org."""
    return render_template("publications.html")
    # redirect("/")


@app.route("/publications/<name>")
def fetchPublication(name):
    """Fetch a publication from the `data` folder"""
    for publication in publications_data:
        if publication["code"] == name:
            with open(os.path.join("data", publication["code"]+".docx"), "rb") as doc:
                pub_text = mammoth.convert_to_html(doc)
                pub_title = publication["title"]
                pub_writers = ', '.join(publication["writers"])
                pub_editors = ', '.join(publication["editors"])
                return render_template("publication.html",
                                        pub_text=pub_text.value,
                                        pub_title=pub_title,
                                        pub_writers=pub_writers,
                                        pub_editors=pub_editors)
    return redirect("/publications")
    # return redirect("/")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Contacts page for the Warbler Org."""
    if request.method == "POST":
        name = request.form.get("visitor_name")
        email = request.form.get("visitor_email")
        subject = request.form.get("visitor_subject")
        message = request.form.get("visitor_message")

        cur.execute("""INSERT INTO contacts (name, email, subject, message, time)
                       VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP);
                    """,
                    (name, email, subject, message))
        conn.commit()

        return redirect("/contact")
    else:
        return render_template("contact.html")


@app.route("/about")
def about():
    """About page for the Warbler Org."""
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
