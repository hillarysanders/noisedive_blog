from noisedive_flask.helpers import (
    session,
    message,
    redirect,
    Blueprint,
    query,  # Add the query utility function here
)

deletePostBlueprint = Blueprint("deletePost", __name__)


@deletePostBlueprint.route("/deletepost/<int:postID>/redirect=<direct>")
def deletePost(postID, direct):
    # TODO: add a 'are you sure' thingy
    if "userName" in session:
        author = query(f"select author from posts where id = ?", (postID,), fetchone=True)
        direct = direct.replace("&", "/")
        if author and author[0] == session["userName"]:
            query(f"delete from posts where id = ?", (postID,), commit=True)
            message("2", f'POST: "{postID}" DELETED')
        else:
            message(
                "1",
                f'POST: "{postID}" NOT DELETED "{postID}" DOES NOT BELONG TO USER: {session["userName"]}',
            )
    else:
        message("1", f'USER NEEDS TO LOGIN FOR DELETE POST: "{postID}"')
    
    return redirect(f"/")