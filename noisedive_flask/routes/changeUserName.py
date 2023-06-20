from noisedive_blog.helpers import (
    session,
    request,
    flash,
    message,
    redirect,
    render_template,
    Blueprint,
    changeUserNameForm,
    query
)

changeUserNameBlueprint = Blueprint("changeUserName", __name__)


@changeUserNameBlueprint.route("/changeusername", methods=["GET", "POST"])
def changeUserName():
    if "userName" in session:
        form = changeUserNameForm(request.form)
        if request.method == "POST":
            newUserName = request.form["newUserName"].replace(" ", "")
            userNameCheck = query(
                "SELECT userName FROM users WHERE userName = ?",
                params=(newUserName,),
                fetchone=True
            )
            if newUserName.isascii():
                if newUserName == session["userName"]:
                    flash("this is your username", "error")
                elif userNameCheck is None:
                    query(
                        "UPDATE users SET userName = ? WHERE userName = ?",
                        params=(newUserName, session["userName"]),
                        commit=True
                    )
                    query(
                        "UPDATE posts SET Author = ? WHERE author = ?",
                        params=(newUserName, session["userName"]),
                        commit=True
                    )
                    query(
                        "UPDATE comments SET user = ? WHERE user = ?",
                        params=(newUserName, session["userName"]),
                        commit=True
                    )
                    message(
                        "2",
                        f'USER: "{session["userName"]}" CHANGED USER NAME TO "{newUserName}"',
                    )
                    session["userName"] = newUserName
                    flash("user name changed", "success")
                    return redirect(f"/user/{newUserName.lower()}")
                else:
                    flash("This username is already taken.", "error")
            else:
                flash("username does not fit ascii characters", "error")

        return render_template("changeUserName.html", form=form)
    else:
        return redirect("/")
