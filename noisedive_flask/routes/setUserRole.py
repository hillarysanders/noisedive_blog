from noisedive_flask.helpers import Blueprint, session, redirect, message, query

setUserRoleBlueprint = Blueprint("setUserRole", __name__)


@setUserRoleBlueprint.route("/setuserrole/<userName>/<newRole>")
def setUserRole(userName, newRole):
    if "userName" in session:
        # Retrieve the role of the current logged-in user
        current_user_role = query(
            "SELECT role FROM users WHERE userName = ?",
            params=(session["userName"],),
            fetchone=True
        )[0]
        # Check if the current logged-in user is an admin
        if current_user_role == "admin":
            # Update the role of the specified user
            query(
                "UPDATE users SET role = ? WHERE lower(userName) = ?",
                params=(newRole, userName.lower()),
                commit=True
            )
            message("2", f'ADMIN: "{session["userName"]}" CHANGED USER: "{userName}"\'s ROLE TO {newRole}')
            return redirect("/admin/users")

    return redirect("/")
