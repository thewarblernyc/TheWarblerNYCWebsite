from flask import Flask, render_template, request, redirect
import psycopg2
import os

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def home():
    """Homepage for the Warbler Org."""
    return render_template("index.html")


@app.route("/publication")
def resource():
    """Publications page for the Warbler Org."""
    return render_template("publication.html")


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
