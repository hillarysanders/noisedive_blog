from noisedive_blog.helpers import (
    session,
    request,
    flash,
    message,
    redirect,
    addPoints,
    currentDate,
    currentTime,
    render_template,
    Blueprint,
    createPostForm,
    query,
)

createPostBlueprint = Blueprint("createPost", __name__)

@createPostBlueprint.route("/createpost", methods=["GET", "POST"])
def createPost():
    if "userName" not in session:
        message("1", "USER NOT LOGGED IN")
        flash("you need login to create a post", "error")
        return redirect("/login")
    
    role = query(f'select role from users where userName = ?', (session["userName"],), fetchone=True)[0]
    if role != "admin":
        flash("Currently only Admins may make posts.", "error")
        # message("1", f"Currently only Admins may make posts.")
        return redirect("/")
    else:
        form = createPostForm(request.form)
        if request.method == "POST":
            postTitle = request.form["postTitle"]
            postTags = request.form["postTags"]
            postContent = request.form["postContent"]
            if postContent == "":
                flash("post content cannot be empty", "error")
                message(
                    "1",
                    f'POST CONTENT NOT BE EMPTY USER: "{session["userName"]}"',
                )
            else:
                current_time = currentTime()
                current_date = currentDate()
                x = query(f"""
                    INSERT INTO posts(title, tags, content, author, views, date, time, lastEditDate, lastEditTime)
                    VALUES(?, ?, ?, ?, 0,
                        "{current_date}", "{current_time}", "{current_date}", "{current_time}")
                """, (postTitle, postTags, postContent, session["userName"],), commit=True)
                # import pdb; pdb.set_trace()
                post_id = query(f"""select id from posts where 
                                        time='{current_time}' and 
                                        date='{current_date}' and
                                        author='{session['userName']}'""")[0].id
                
                message("2", f'POST: "{postTitle}" POSTED')
                addPoints(20, session["userName"])
                flash("You earned 20 points by posting ", "success")
                return redirect(f"/post/{post_id}")
        return render_template("createPost.html", form=form)
