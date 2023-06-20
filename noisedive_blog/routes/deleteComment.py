from noisedive_blog.helpers import (
    session,
    message,
    redirect,
    Blueprint,
    query
)

deleteCommentBlueprint = Blueprint("deleteComment", __name__)


@deleteCommentBlueprint.route("/deletecomment/<int:commentID>/redirect=<direct>")
def deleteComment(commentID, direct):
    direct = direct.replace("&", "/")
    if "userName" in session:
        user = query(
            "SELECT user FROM comments WHERE id = ?",
            params=(commentID,),
            fetchone=True,
        )
        if user and user[0] == session["userName"]:
            query("DELETE FROM comments WHERE id = ?", params=(commentID,), commit=True)
            message("2", f'COMMENT: "{commentID}" DELETED')
        else:
            message(
                "1",
                f'COMMENT: "{commentID}" NOT DELETED "{commentID}" DOES NOT BELONG TO {session["userName"]}',
            )
    else:
        message("1", f"USER NEEDS TO LOGIN FOR DELETE COMMENT: {commentID}")
        
    return redirect(f"/{direct}")