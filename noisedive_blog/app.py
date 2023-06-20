import sys
import os
import json
# Get the directory above the directory containing the current script (__file__)
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # local:
# sys.path.append(current_dir)
# # are these even needed? Maybe not because it's a package. TODO: test.
# # production:
sys.path.append('/home/protected/noisedive')
# # if not found there, search in public:
# sys.path.append('/home/public/')
from datetime import timedelta
import socket
from noisedive_blog.helpers import (
    secrets,
    message,
    render_template,
    getProfilePicture,
    Flask,
)

message(1, 'HELLO 2!')
message(1, sys.path)

from noisedive_blog.routes.post import postBlueprint
from noisedive_blog.routes.user import userBlueprint
from noisedive_blog.routes.index import indexBlueprint
from noisedive_blog.routes.login import loginBlueprint
from noisedive_blog.routes.signup import signUpBlueprint
from noisedive_blog.routes.logout import logoutBlueprint
from noisedive_blog.routes.search import searchBlueprint
# from noisedive_blog.routes.searchBar import searchBarBlueprint
from noisedive_blog.routes.editPost import editPostBlueprint
from noisedive_blog.routes.dashboard import dashboardBlueprint
from noisedive_blog.routes.adminPanel import adminPanelBlueprint
from noisedive_blog.routes.deleteUser import deleteUserBlueprint
from noisedive_blog.routes.deletePost import deletePostBlueprint
from noisedive_blog.routes.createPost import createPostBlueprint
from noisedive_blog.routes.setUserRole import setUserRoleBlueprint
from noisedive_blog.routes.deleteComment import deleteCommentBlueprint
from noisedive_blog.routes.changeUserName import changeUserNameBlueprint
from noisedive_blog.routes.changePassword import changePasswordBlueprint
from noisedive_blog.routes.adminPanelUsers import adminPanelUsersBlueprint
from noisedive_blog.routes.adminPanelPosts import adminPanelPostsBlueprint
from noisedive_blog.routes.accountSettings import accountSettingsBlueprint
from noisedive_blog.routes.adminPanelComments import adminPanelCommentsBlueprint
from noisedive_blog.dbChecker import check_if_db_dir_exists, check_if_db_exists, usersTable, postsTable, commentsTable




def create_app():

    print('HELLO')
    message(1, 'HELLO!')
    print(sys.path)
    message(1, "check_if_db_dir_exists")
    check_if_db_dir_exists()
    message(1, "check_if_db_exists")
    check_if_db_exists()
    message(1, "making usersTable")
    usersTable()
    message(1, "making postsTable")
    postsTable()
    commentsTable()

    app = Flask(__name__)
    app.secret_key = secrets.token_urlsafe(32)
    app.config["SESSION_PERMANENT"] = True
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=30)

    @app.context_processor
    def utility_processor():
        getProfilePicture
        return dict(getProfilePicture=getProfilePicture)


    @app.errorhandler(404)
    def notFound(e):
        message("1", str(e))  # TODO: remove, temp
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
    # app.register_blueprint(searchBarBlueprint)
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

if __name__ == "__main__":
    app = create_app()
    app.run(debug=False, host=socket.gethostbyname(socket.gethostname()))
