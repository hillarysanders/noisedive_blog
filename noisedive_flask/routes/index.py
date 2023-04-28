from noisedive_flask.helpers import (
    sqlite3,
    render_template,
    Blueprint,
    query
)

indexBlueprint = Blueprint("index", __name__)


@indexBlueprint.route("/")
def index():
    return render_template(
        "index.html",
        posts=query("select * from posts"),
    )
