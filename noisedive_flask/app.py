import sys
import os
sys.path.append(os.getcwd())
sys.path.append('/home/public/noisedive_flask')
sys.path.append('/home/protected/noisedive/noisedive_flask')

import socket
from noisedive_flask.helpers import (
    secrets,
    message,
    render_template,
    getProfilePicture,
    Flask,
)

from noisedive_flask.routes.post import postBlueprint
from noisedive_flask.routes.user import userBlueprint
from noisedive_flask.routes.index import indexBlueprint
from noisedive_flask.routes.login import loginBlueprint
from noisedive_flask.routes.signup import signUpBlueprint
from noisedive_flask.routes.logout import logoutBlueprint
from noisedive_flask.routes.search import searchBlueprint
from noisedive_flask.routes.searchBar import searchBarBlueprint
from noisedive_flask.routes.editPost import editPostBlueprint
from noisedive_flask.routes.dashboard import dashboardBlueprint
from noisedive_flask.routes.adminPanel import adminPanelBlueprint
from noisedive_flask.routes.deleteUser import deleteUserBlueprint
from noisedive_flask.routes.deletePost import deletePostBlueprint
from noisedive_flask.routes.createPost import createPostBlueprint
from noisedive_flask.routes.setUserRole import setUserRoleBlueprint
from noisedive_flask.routes.deleteComment import deleteCommentBlueprint
from noisedive_flask.routes.changeUserName import changeUserNameBlueprint
from noisedive_flask.routes.changePassword import changePasswordBlueprint
from noisedive_flask.routes.adminPanelUsers import adminPanelUsersBlueprint
from noisedive_flask.routes.adminPanelPosts import adminPanelPostsBlueprint
from noisedive_flask.routes.accountSettings import accountSettingsBlueprint
from noisedive_flask.routes.adminPanelComments import adminPanelCommentsBlueprint
from dbChecker import check_if_db_dir_exists, check_if_db_exists, usersTable, postsTable, commentsTable


def create_app():

    check_if_db_dir_exists()
    check_if_db_exists()
    usersTable()
    postsTable()
    commentsTable()

    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(32)
    app.config["SESSION_PERMANENT"] = True

    @app.context_processor
    def utility_processor():
        getProfilePicture
        return dict(getProfilePicture=getProfilePicture)


    @app.errorhandler(404)
    def notFound(e):
        message("1", "404", str(e))  # TODO: remove, temp
        return render_template("404.html"), 404

    app.register_blueprint(postBlueprint)
    app.register_blueprint(userBlueprint)
    app.register_blueprint(indexBlueprint)
    app.register_blueprint(loginBlueprint)
    app.register_blueprint(signUpBlueprint)
    app.register_blueprint(logoutBlueprint)
    app.register_blueprint(searchBlueprint)
    app.register_blueprint(editPostBlueprint)
    app.register_blueprint(dashboardBlueprint)
    app.register_blueprint(searchBarBlueprint)
    app.register_blueprint(adminPanelBlueprint)
    app.register_blueprint(deleteUserBlueprint)
    app.register_blueprint(deletePostBlueprint)
    app.register_blueprint(createPostBlueprint)
    app.register_blueprint(setUserRoleBlueprint)
    app.register_blueprint(deleteCommentBlueprint)
    app.register_blueprint(changeUserNameBlueprint)
    app.register_blueprint(changePasswordBlueprint)
    app.register_blueprint(adminPanelUsersBlueprint)
    app.register_blueprint(adminPanelPostsBlueprint)
    app.register_blueprint(accountSettingsBlueprint)
    app.register_blueprint(adminPanelCommentsBlueprint)

    return app

match __name__:
    case "__main__":
        app = create_app()
        app.run(debug=False, host=socket.gethostbyname(socket.gethostname()))
