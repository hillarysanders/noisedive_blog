from noisedive_flask.helpers import (
    session,
    request,
    sqlite3,
    flash,
    message,
    redirect,
    addPoints,
    render_template,
    Blueprint,
    loginForm,
    sha256_crypt,
    query,
)

loginBlueprint = Blueprint("login", __name__)


@loginBlueprint.route("/login/redirect=<direct>", methods=["GET", "POST"])
def login(direct):
    direct = direct.replace("&", "/")
    if "userName" in session:
        message("1", f'USER: "{session["userName"]}" ALREADY LOGGED IN')
        return redirect(direct)
    else:
        form = loginForm(request.form)
        if request.method == "POST":
            userName = request.form["userName"]
            password = request.form["password"]
            user = query(f'select * from users where lower(userName) = ?', (userName.lower(),), fetchone=True)
            if not user:
                message("1", f'USER: "{userName}" NOT FOUND')
                flash("user not found", "error")
            else:
                if sha256_crypt.verify(password, user.password):
                    session["userName"] = user.username
                    session.permanent = True # make the session a permanent session.
                    addPoints(1, session["userName"])
                    message("2", f'USER: "{user.username}" LOGGED IN')
                    flash(f"Welcome {user.username}", "success")
                    return redirect(direct)
                else:
                    message("1", "WRONG PASSWORD")
                    flash("wrong  password", "error")
        return render_template("login.html", form=form, hideLogin=True)
