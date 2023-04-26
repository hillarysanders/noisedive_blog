import os
import secrets
import sqlite3
from os import mkdir
from os.path import exists
from datetime import datetime
from passlib.hash import sha256_crypt
from flask import render_template, Blueprint
from forms import (
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

def get_sqlite_cursor_and_connection(table_name):
    # if table_name not in ['users', 'posts', 'comments']:
    #      # some warning
     # Construct the absolute paths to the database files
    if not table_name.endswith('.db'):
         table_name = f'{table_name}.db'
    db_path = os.path.join(basedir, 'db', table_name)
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    return cursor, connection
    
def get_sqlite_cursor(table_name):
    cursor, _ = get_sqlite_cursor_and_connection(table_name)
    return cursor

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
    cursor, connection = get_sqlite_cursor_and_connection('users.db')
    cursor.execute(
        f'update users set points = points+{points} where userName = "{user}"'
    )
    connection.commit()
    message("2", f'{points} POINTS ADDED TO "{user}"')


def getProfilePicture(userName):
    cursor = get_sqlite_cursor('users.db')
    cursor.execute(
        f'select profilePicture from users where lower(userName) = "{userName.lower()}"'
    )
    return cursor.fetchone()[0]
