import markdown
from noisedive_flask.helpers import (
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
    apply_markdown_with_latex
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
        print(post[3])
        return render_template(
            "post.html",
            # horrible. Should be named dictionary!
            id=post[0],
            title=post[1],
            tags=post[2],
            content=apply_markdown_with_latex(post[3]),
            author=post[4],
            views=post[7],
            date=post[5],
            time=post[6],
            form=form,
            comments=comments,
        )