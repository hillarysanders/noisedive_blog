from noisedive_flask.helpers import (
    session,
    request,
    flash,
    message,
    redirect,
    render_template,
    Blueprint,
    sha256_crypt,
    changePasswordForm,
    query
)

changePasswordBlueprint = Blueprint("changePassword", __name__)


@changePasswordBlueprint.route("/changepassword", methods=["GET", "POST"])
def changePassword():
    if "userName" in session:
        form = changePasswordForm(request.form)
        if request.method == "POST":
            oldPassword = request.form["oldPassword"]
            password = request.form["password"]
            passwordConfirm = request.form["passwordConfirm"]
            stored_password = query(
                "SELECT password FROM users WHERE userName = ?",
                params=(session["userName"],),
                fetchone=True
            )[0]
            if sha256_crypt.verify(oldPassword, stored_password):
                if oldPassword == password:
                    flash("New password can't be the same as the old password", "error")
                    message("1", "NEW PASSWORD CAN'T BE SAME AS OLD PASSWORD")
                elif password != passwordConfirm:
                    message("1", "PASSWORDS MUST MATCH")
                    flash("Passwords must match", "error")
                elif oldPassword != password and password == passwordConfirm:
                    newPassword = sha256_crypt.hash(password)
                    query(
                        "UPDATE users SET password = ? WHERE userName = ?",
                        params=(newPassword, session["userName"]),
                        commit=True
                    )
                    message("2", f'USER: "{session["userName"]}" CHANGED THEIR PASSWORD')
                    session.clear()
                    flash("Your password has been changed.", "success")
                    return redirect("/login")
            else:
                flash("Old password is incorrect", "error")
                message("1", "OLD PASSWORD INCORRECT")

        return render_template("changePassword.html", form=form)
    else:
        message("1", "USER NOT LOGGED IN")
        flash("You need to log in to change your password", "error")
        return redirect("/login")
