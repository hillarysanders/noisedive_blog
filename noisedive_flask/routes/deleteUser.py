from noisedive_flask.helpers import (
    session,
    sqlite3,
    message,
    redirect,
    Blueprint,
    query,
    commit_to_db
)

deleteUserBlueprint = Blueprint("deleteUser", __name__)

@deleteUserBlueprint.route("/deleteuser/<userName>/redirect=<direct>")
def deleteUser(userName, direct):
    direct = direct.replace("&", "/")
    if "userName" in session:
        user = query(f'select * from users where lower(userName) = "{userName.lower()}"', fetchone=True)
        perpetrator = query(f'select role from users where userName = "{session["userName"]}"', fetchone=True)
        if user is None:
            return redirect(f"/{direct}")
        else:
            if user[1] == session["userName"] or perpetrator[0] == "admin":
                commit_to_db(
                    f'delete from users where lower(userName) = "{userName}"'
                )
                commit_to_db(f"update sqlite_sequence set seq = seq-1")

                if perpetrator[0] != "admin":
                    session.clear()

            return redirect(f"{direct}")    

    else:
        return redirect(f"/login/redirect=&deleteuser&{userName}&redirect=index")
