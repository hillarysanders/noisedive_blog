import os
import secrets
import sqlite3
from os import mkdir
from os.path import exists
from datetime import datetime
from passlib.hash import sha256_crypt
from flask import render_template, Blueprint
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
DB_DIR = 'noisedive_flask/db'
DB_PATH = os.path.join(DB_DIR, DB_NAME)

def get_sqlite_cursor_and_connection(db_path=DB_PATH):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    return cursor, connection
    
def get_sqlite_cursor(table_name):
    cursor, _ = get_sqlite_cursor_and_connection(table_name)
    return cursor

# TODO: return named dictionary (attrs)
def query(query_str, fetchone=False):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        if fetchone:
             results = cursor.execute(query_str).fetchone()
        else:
             results = cursor.execute(query_str).fetchall()
        cursor.close()
        return results
        
def commit_to_db(query_str):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query_str)
        cursor.close()


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
    commit_to_db(f'update users set points = points+{points} where userName = "{user}"')

def getProfilePicture(userName):
    return query(f'select profilePicture from users where lower(userName) = "{userName.lower()}"', fetchone=True)[0]
    