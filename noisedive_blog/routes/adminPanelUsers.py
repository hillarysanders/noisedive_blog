from noisedive_blog.helpers import render_template, Blueprint, session, redirect, query

adminPanelUsersBlueprint = Blueprint("adminPanelUsers", __name__)

@adminPanelUsersBlueprint.route("/admin/users")
@adminPanelUsersBlueprint.route("/adminpanel/users")
def adminPanelUsers():
    if "userName" in session:
        role = query(f'select role from users where userName = ?', (session["userName"],), fetchone=True)[0]
        if role == "admin":
            users = query("select * from users")
            return render_template("adminPanelUsers.html", users=users)
    return redirect("/")