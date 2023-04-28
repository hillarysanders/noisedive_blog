from noisedive_flask.helpers import (
    session,
    secrets,
    request,
    flash,
    get_sqlite_cursor_and_connection,
    message,
    redirect,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    signUpForm,
    sha256_crypt,
    query
    
)

signUpBlueprint = Blueprint("signup", __name__)


@signUpBlueprint.route("/signup", methods=["GET", "POST"])
def signup():
    if "userName" in session:
        return redirect("/")
    
    form = signUpForm(request.form)
    success = True
    if request.method == "POST":
        userName = request.form["userName"]
        email = request.form["email"]
        password = request.form["password"]
        passwordConfirm = request.form["passwordConfirm"]
        if query("select userName from users where userName={userName}"):
            flash("This username is unavailable.", "error")
            success = False

        if query("select email from users where email={email}"):
            flash("This email is unavailable.", "error")
            success = False

        if passwordConfirm != password:
            flash("Passwords do not match.", "error")
            success = False

        if not userName.isascii():
            flash("username does not fit ascii charecters", "error")
            success = False

        if success:
            password = sha256_crypt.hash(password)
            query(
                f"""
                insert into users(userName,email,password,profilePicture,role,points,creationDate,creationTime) 
                values("{userName}",
                "{email}",
                "{password}",
                "https://api.dicebear.com/5.x/identicon/svg?seed={secrets.token_urlsafe(32)}",
                "user",
                0,
                "{currentDate()}",
                "{currentTime()}")
                """, commit=True
            )
    return render_template("signup.html", form=form, hideSignUp=True)
