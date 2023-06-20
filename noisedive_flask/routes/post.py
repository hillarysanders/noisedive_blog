import markdown
from noisedive_blog.helpers import (
    session,
    sqlite3,
    request,
    flash,
    message,
    redirect,
    addPoints,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    commentForm,
    query,
    convert_row_and_apply_markdown
)

postBlueprint = Blueprint("post", __name__)


@postBlueprint.route("/post/<int:postID>", methods=["GET", "POST"])
def post(postID):
    form = commentForm(request.form)
    post = query(f'select * from posts where id = ?', (postID,), fetchone=True)
    if len(post)==0:
        message("1", "404")
        return render_template("404.html")
    else:
        query(f'update posts set views = views+1 where id = ?', (postID,), commit=True)
        if request.method == "POST":
            comment = request.form["comment"]
            query(f"""
                    insert into comments(post,comment,user,date,time)
                    values({postID},"{comment}","{session["userName"]}",
                    "{currentDate()}",
                    "{currentTime()}")
                    """, commit=True)
            addPoints(5, session["userName"])
            flash("You earned 5 points by commenting ", "success")
            return redirect(f"/post/{postID}")
        
        comments = query('select * from comments where post = ?', (postID,))
        print(post.content)
        print('\n\n\n')
        print(convert_row_and_apply_markdown([post])[0].content)

        return render_template(
            "post.html",
            # post=post,
            post=convert_row_and_apply_markdown([post])[0],
            form=form,
            comments=comments,
        )