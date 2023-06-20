from noisedive_blog.helpers import (
    session,
    request,
    flash,
    message,
    redirect,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    createPostForm,
    query,
)

editPostBlueprint = Blueprint("editPost", __name__)

@editPostBlueprint.route("/editpost/<int:postID>", methods=["GET", "POST"])
def editPost(postID):
    if "userName" in session:
        posts = query("select id from posts")
        if (postID,) in posts:
            post = query(f"select * from posts where id = ?", (postID,), fetchone=True)
            message("2", f'POST: "{postID}" FOUND')
            if post[4] == session["userName"]:
                form = createPostForm(request.form)
                form.postTitle.data = post[1]
                form.postTags.data = post[2]
                form.postContent.data = post[3]
                if request.method == "POST":
                    postTitle = request.form["postTitle"]
                    postTags = request.form["postTags"]
                    postContent = request.form["postContent"]
                    if postContent != "":
                        query(
                            f'''
                            update posts set title = ?, tags = ?, content = ?, lastEditDate = ?, lastEditTime = ?
                            where id = ?
                            ''',
                            (postTitle, postTags, postContent, currentDate(), currentTime(), post[0]),
                            commit=True
                        )
                        message("2", f'POST: "{postTitle}" EDITED')
                        flash("Post edited", "success")
                        return redirect(f"/post/{post[0]}")
                    else:
                        flash("post content cannot be empty", "error")
                        message(
                            "1",
                            f'POST CONTENT CANNOT BE EMPTY USER: "{session["userName"]}"',
                        )

                return render_template(
                    "/editPost.html",
                    title=post[1],
                    tags=post[2],
                    content=post[3],
                    form=form,
                )
            else:
                flash("this post does not belong to you", "error")
                message(
                    "1",
                    f'THIS POST DOES NOT BELONG TO USER: "{session["userName"]}"',
                )
                return redirect("/")
        else:
            message("1", f'POST: "{postID}" NOT FOUND')
            return render_template("404.html")
    else:
        message("1", "USER NOT LOGGED IN")
        flash("you need to log in to edit a post", "error")
        return redirect("/login")