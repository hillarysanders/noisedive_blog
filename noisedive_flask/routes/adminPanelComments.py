from noisedive_flask.helpers import render_template, Blueprint, session, redirect, query

adminPanelCommentsBlueprint = Blueprint("adminPanelComments", __name__)

@adminPanelCommentsBlueprint.route("/admin/comments")
@adminPanelCommentsBlueprint.route("/adminpanel/comments")
def adminPanelComments():
    if "userName" in session:
        role = query(f'select role from users where userName = ?', (session["userName"],), fetchone=True)[0]
        if role == "admin":
            comments = query("select * from comments")
            return render_template("adminPanelComments.html", comments=comments)
    return redirect("/")