from noisedive_flask.helpers import sqlite3, render_template, Blueprint, session, redirect, query

adminPanelBlueprint = Blueprint("adminPanel", __name__)


@adminPanelBlueprint.route("/admin")
def adminPanel():
    if "userName" in session:
        role = query(f'select role from users where userName = ?', (session["userName"],), fetchone=True)[0]
        if role == "admin":
            return render_template("adminPanel.html")

    return redirect("/")
