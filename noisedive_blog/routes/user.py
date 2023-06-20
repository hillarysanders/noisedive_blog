import sqlite3
from noisedive_blog.helpers import (
    message,
    render_template,
    Blueprint,
    query
)

userBlueprint = Blueprint("user", __name__)


@userBlueprint.route("/user/<userName>")
def user(userName):
    user = query(f'select * from users where lower(userName) = ?', (userName,), fetchone=True)
    if len(user)==0:
        message("1", f'USER: "{userName}" NOT FOUND')
        return render_template("404.html")
    else:
        viewsData = query(f'select views from posts where author = ?', (user.username,))
        views = 0
        # TODO: why for loop here??
        for view in viewsData:
            views += int(view[0])
        posts = query(f'select * from posts where author = ?', (user.username,))
        comments = query(f'select * from comments where lower(user) = ?', (user.username,))
        return render_template(
            "user.html",
            user=user,
            views=views,
            posts=posts,
            comments=comments,
            showPosts=len(posts)>0,
            showComments=len(comments)>0,
        )
