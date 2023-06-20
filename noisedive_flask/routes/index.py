from noisedive_blog.helpers import (
    sqlite3,
    render_template,
    Blueprint,
    query,
    convert_row_and_apply_markdown
)

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    # print([post.id for post in query("select * from posts")])
    # x = convert_row_and_apply_markdown(query("select * from posts")[::-1])
    
    return render_template(
        "index.html",
        # posts=query("select * from posts")[::-1],
        posts=convert_row_and_apply_markdown(query("select * from posts")[::-1]),
    )
