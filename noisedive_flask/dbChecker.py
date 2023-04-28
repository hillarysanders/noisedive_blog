import os
import sqlite3
from noisedive_flask.helpers import query, mkdir, exists, message, DB_DIR, DB_PATH

def check_if_db_dir_exists():
    if exists(DB_DIR):
        message("6", f'Folder: {DB_DIR} FOUND')
    else:
        message("1", f'Folder: {DB_DIR} NOT FOUND')
        mkdir(DB_DIR)
        message("2", f'Folder: {DB_DIR} CREATED')


def check_if_db_exists():
    match exists(DB_PATH):
        case True:
            message("6", f'DATABASE: {DB_PATH} FOUND')
        case False:
            message("1", f'DATABASE: {DB_PATH} NOT FOUND')
            open(DB_PATH, "x")
            message("2", f'DATABASE: {DB_PATH} CREATED')


def check_if_table_exists(table_name):
    exists = query(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    return exists is not None


def usersTable():
    if not check_if_table_exists('users'):
        query("""
        CREATE TABLE IF NOT EXISTS users(
	    "userID"	INTEGER NOT NULL UNIQUE,
	    "userName"	TEXT UNIQUE,
	    "email"	TEXT UNIQUE,
	    "password"	TEXT,
        "profilePicture" TEXT,
	    "role"	TEXT,
	    "points"	INTEGER,
	    "creationDate"	TEXT,
	    "creationTime"	TEXT,
	    PRIMARY KEY("userID" AUTOINCREMENT)
        );""", commit=True)


def postsTable():
    if not check_if_table_exists('posts'):
        query("""
            CREATE TABLE "posts" (
            "id"	INTEGER NOT NULL UNIQUE,
            "title"	TEXT NOT NULL,
            "tags"	TEXT,
            "content"	TEXT NOT NULL,
            "author"	TEXT NOT NULL,
            "date"	TEXT NOT NULL,
            "time"	TEXT NOT NULL,
            "views"	TEXT,
            "lastEditDate"	TEXT,
            "lastEditTime"	TEXT,
            PRIMARY KEY("id" AUTOINCREMENT)
            );""", commit=True)



def commentsTable():
    if not check_if_table_exists('comments'):
        query("""
        CREATE TABLE IF NOT EXISTS comments(
	    "id"	INTEGER NOT NULL,
	    "post"	INTEGER,
	    "comment"	TEXT,
	    "user"	TEXT,
	    "date"	TEXT,
	    "time"	TEXT,
	    PRIMARY KEY("id" AUTOINCREMENT)
        );""", commit=True)
