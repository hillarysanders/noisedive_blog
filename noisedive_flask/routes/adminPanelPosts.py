from noisedive_blog.helpers import render_template, Blueprint, session, redirect, query

adminPanelPostsBlueprint = Blueprint("adminPanelPosts", __name__)

@adminPanelPostsBlueprint.route("/admin/posts")
@adminPanelPostsBlueprint.route("/adminpanel/posts")
def adminPanelPosts():
    if "userName" in session:
        role = query(f'select role from users where userName = ?', (session["userName"],), fetchone=True)[0]
        if role == "admin":
            posts = query("select * from posts")
            return render_template("dashboard.html", posts=posts, showPosts=True)
    return redirect("/")