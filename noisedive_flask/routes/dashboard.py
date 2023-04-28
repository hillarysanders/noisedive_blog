from noisedive_flask.helpers import (
    session,
    flash,
    message,
    redirect,
    render_template,
    Blueprint,
    query,
)

dashboardBlueprint = Blueprint("dashboard", __name__)

@dashboardBlueprint.route("/dashboard/<userName>")
def dashboard(userName):
    if "userName" in session:
        if session["userName"].lower() == userName.lower():
            posts = query(f'select * from posts where author = "{session["userName"]}"')
            comments = query(f'select * from comments where lower(user) = "{userName.lower()}"')
            showPosts = bool(posts)
            showComments = bool(comments)
            return render_template(
                "/dashboard.html",
                posts=posts,
                comments=comments,
                showPosts=showPosts,
                showComments=showComments,
            )
        else:
            message(
                "1",
                f'THIS IS DASHBOARD NOT BELONGS TO USER: "{session["userName"]}"',
            )
            return redirect(f'/dashboard/{session["userName"].lower()}')
    else:
        message("1", "DASHBOARD CANNOT BE ACCESSED WITHOUT USER LOGIN")
        flash("you need login to access the dashboard", "error")
        return redirect("/login/redirect=&dashboard&user")