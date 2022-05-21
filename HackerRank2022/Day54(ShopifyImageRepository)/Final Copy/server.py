from flask import Flask, render_template, request
import sqlite3
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askopenfilenames  # pop open file choice
from os.path import exists  # Check if file exists
import base64
from werkzeug.utils import secure_filename
from io import BytesIO
import os

current_directory = os.getcwd()

app = Flask(__name__)


def get_cursor():
    conn = sqlite3.connect("SQLite_Python.db")
    cur = conn.cursor()
    return (cur, conn)


"""Initialize the sqlite database and fill up the `products` table with sample data."""


def initialize_db():
    db_exists = exists(
        f"{current_directory}\SQLite_Python.db")

    if db_exists:
        print('DB DOES EXIST')

    if not db_exists:
        print('DB DOES NOT EXIST')
        # Create initial table
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('''CREATE TABLE new_employee
                        (id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);''')
        sqliteConnection.commit()
    print("Initialized database")


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(empId, name, photo):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO new_employee
                                  (id, name, photo) VALUES ( ?, ?, ?)"""
        empPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        data_tuple = (empId, name, empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

@app.route("/")
def home_page():
    (cur, conn) = get_cursor()
    cur.execute("SELECT rowid, * FROM new_employee")

    rows = cur.fetchall()
    print("Retrieved %d database entries" % len(rows))

    # Pre-process product info for HTML templates
    products = []
    for row in rows:
        products.append({
            "id": row[0],
            "name": row[1],
            "photo": row[2],
            "image": row[3].decode()
            # "image": row[3]
        })
    return render_template("index.html", products=products)





# @app.route("/addPhoto/", methods=['POST'])
# def addPhoto():
#     pics = request.files['files']
#     pic = request.files.getlist('files')
#
#     if not pics:
#         return "No pic uploaded!", 400
#
#     filename = secure_filename(pics.filename)
#     mimetype = pics.mimetype
#
#     if not filename or not mimetype:
#         return "Bad upload!", 400
#
#     for count, i in enumerate(pic):
#         sqliteConnection = sqlite3.connect('SQLite_Python.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")
#         sqlite_addPhoto_query = """ INSERT INTO new_employee
#                                           (id, name, photo) VALUES ( ?, ?, ?)"""
#         photoBytes = i.read()
#         photoData = base64.b64encode(photoBytes)
#         # Convert data into tuple format
#         data_tuple = (count+1, 'Joe', photoData)
#         cursor.execute(sqlite_addPhoto_query, data_tuple)
#         sqliteConnection.commit()
#         print("Image and file inserted successfully as a BLOB into a table")
#         cursor.close()
#     return 'Img Uploaded!', 200

@app.route("/addPhoto/", methods=['POST'])
def addPhoto():
    pics = request.files['files']
    pic = request.files.getlist('files')

    if not pics:
        return "No pic uploaded!", 400

    filename = secure_filename(pics.filename)
    mimetype = pics.mimetype

    if not filename or not mimetype:
        return "Bad upload!", 400

    # Grabbing final row from db for ID numbering reasons
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    cursor.execute("SELECT id FROM new_employee ORDER BY id DESC LIMIT 1")
    finalEntryID = cursor.fetchone()

    for count, i in enumerate(pic, 1):
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        photoBytes = i.read()
        photoData = base64.b64encode(photoBytes)
        if finalEntryID is None:
            finalEntryID = [0]
        # Convert data into tuple format
        data_tuple = (count+finalEntryID[0], 'Joe', photoData)
        sqlite_addPhoto_query = """ INSERT INTO new_employee
                                          (id, name, photo) VALUES ( ?, ?, ?)"""
        cursor.execute(sqlite_addPhoto_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()
    return 'Image(s) Uploaded! Press the back button and refresh the page.', 200

# @app.route("/image/:id", methods=['GET'])
# def image():


@app.route("/reset")
def reset():
    # initialize_db()
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DROP TABLE IF EXISTS new_employee")
    cursor.execute('''CREATE TABLE new_employee
                    (id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);''')
    sqliteConnection.commit()
    return render_template("reset.html", message="Database reset. Press the back button and refresh the page.")


if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)