import os
import secrets
import sqlite3
from os import mkdir
from os.path import exists
from datetime import datetime
from passlib.hash import sha256_crypt
from flask import render_template, Blueprint
from collections import namedtuple
from noisedive_flask.forms import (
    loginForm,
    signUpForm,
    commentForm,
    createPostForm,
    changePasswordForm,
    changeUserNameForm,
)
from flask import (
    request,
    session,
    flash,
    redirect,
    render_template,
    send_from_directory,
    Flask,
    Blueprint,
)
basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'sqlite.db'
DB_DIR = os.path.join(basedir, 'db')
# DB_DIR = 'noisedive_flask/db'
DB_PATH = os.path.join(DB_DIR, DB_NAME)

# def get_sqlite_cursor_and_connection(db_path=DB_PATH):
#     connection = sqlite3.connect(db_path)
#     cursor = connection.cursor()
#     return cursor, connection
    
# def get_sqlite_cursor(table_name):
#     cursor, _ = get_sqlite_cursor_and_connection(table_name)
#     return cursor

def named_tuple_row_factory(cursor, row):
    # Define a namedtuple class based on the cursor description (column names)
    columns = [column[0].lower() for column in cursor.description]
    Row = namedtuple("Row", columns)
    # Create a namedtuple instance using the row data
    return Row(*row)


def query(query_str, params=None, fetchone=False, commit=False):
    with sqlite3.connect(DB_PATH) as conn:
        # Set the row_factory attribute to the named_tuple_row_factory (important for code clarity, stability, ease!)
        conn.row_factory = named_tuple_row_factory
        cursor = conn.cursor()
        if params is None:
            # Use an empty tuple if no parameters are provided
            params = ()
        # Execute the query with the parameters
        cursor.execute(query_str, params)
        # If the query is a commit operation, commit the changes
        if commit:
            conn.commit()
            results = None
        else:
            # Fetch the results based on the 'fetchone' argument
            results = cursor.fetchone() if fetchone else cursor.fetchall()
            # # Convert the results to dictionaries
            # results = [dict(row) for row in results] if results else None
        cursor.close()
        return results
    
def currentDate():
    return datetime.now().strftime("%d.%m.%y")


def currentTime(seconds=False):
    if seconds is False:
            return datetime.now().strftime("%H:%M")
    if seconds is True:
            return datetime.now().strftime("%H:%M:%S")


def message(color, message):
    print(
        f"\n\033[94m[{currentDate()}\033[0m"
        f"\033[95m {currentTime(True)}]\033[0m"
        f"\033[9{color}m {message}\033[0m\n"
    )
    logFile = open("log.log", "a")
    logFile.write(f"[{currentDate()}" f"|{currentTime(True)}]" f" {message}\n")
    logFile.close()


def addPoints(points, user):
    query(f'update users set points = points+? where userName = ?', (points, user,), commit=True)

def getProfilePicture(userName):
    return query(f'select profilePicture from users where lower(userName) = ?', (userName.lower(),), fetchone=True)[0]
    