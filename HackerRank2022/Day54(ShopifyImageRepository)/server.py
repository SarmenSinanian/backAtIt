from flask import Flask, render_template
import sqlite3
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askopenfilenames # pop open file choice
from os.path import exists # Check if file exists

# db_exists = exists(r"C:\Users\Sarmen\PycharmProjects\HelloWorld1\2022_Programming\backAtIt\HackerRank2022\Day54(ShopifyImageRepository)\SQLite_Python.db")

# # Prevent redundant table creation
# if not db_exists:
#     # Create initial table
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     cursor.execute('''CREATE TABLE new_employee
#                     ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);''')
#     sqliteConnection.commit()

app = Flask(__name__)

def get_cursor():
    conn = sql.connect("database.db")
    cur = conn.cursor()
    return (cur, conn)

"""Initialize the sqlite database and fill up the `products` table with sample data."""
def initialize_db():
    db_exists = exists(r"C:\Users\Sarmen\PycharmProjects\HelloWorld1\2022_Programming\backAtIt\HackerRank2022\Day54(ShopifyImageRepository)\SQLite_Python.db")
    if not db_exists:
        # Create initial table
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        cursor.execute('''CREATE TABLE new_employee
                        ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);''')
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

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readBlobData(empId):
    try:
        sqliteConnection = sqlite3.connect('SQLite_Python.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sql_fetch_blob_query = """SELECT * from new_employee where id = ?"""
        cursor.execute(sql_fetch_blob_query, (empId,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name = row[1]
            photo = row[2]
            print("Storing employee image and resume on disk \n")
            photoPath = r"C:\Users\Sarmen\PycharmProjects\HelloWorld1\2022_Programming\backAtIt\HackerRank2022\Day54(ShopifyImageRepository)\\" + name + ".jpg"
            writeTofile(photo, photoPath)
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

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
            "id":    row[0],
            "name":  row[1],
            # # image path ***ACTUALLY DON'T NEED PATH; LOADING FROM SQLITE***
            # "src":   "/static/%s" % (row[2]),
            "photo": row[2],
            # "stock": "%d left" % (row[4]),
        })
    
    # # Display total sales so far
    # cur.execute("SELECT SUM(value) FROM transactions")
    # result = cur.fetchone()[0]
    # earnings = result/100.0 if result else 0

    # return render_template("index.html", products=products, earnings=earnings)
    return render_template("index.html", products=products)

@app.route("/addPhoto/")
def addPhoto():
    # Custom photo insert test (as many photos as you want)
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilenames(title='Choose a photo to upload')
    print(filename)
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT id FROM new_employee ORDER BY id DESC LIMIT 1")
    finalEntryID = cursor.fetchone()
    print(finalEntryID)
    sqliteConnection.close()
    # Adding photos from selected photos on previous action; filename = full path
    for count, file in enumerate(filename):
        insertBLOB(count + finalEntryID[0], filename,  'Ally', file)

@app.route("/buy/<product_id>")
def buy(product_id):
    if not product_id:
        return render_template("message.html", message="Invalid product ID!")

    (cur, conn) = get_cursor()

    cur.execute("SELECT rowid, price, stock FROM products WHERE rowid = ?", (product_id,))
    result = cur.fetchone()

    if not result:
        return render_template("message.html", message="Invalid product ID!")
    (rowid, price, stock) = result

    if stock <= 0:
        return render_template("message.html", message="Insufficient stock!")

    print("Processed transaction of value $%.2f" % (price/100.0))
    cur.execute("INSERT INTO transactions (timestamp, productid, value) VALUES " + \
        "(datetime(), ?, ?)", (rowid, price))

    cur.execute("UPDATE products SET stock = stock - 1 WHERE rowid = ?", (product_id,))
    conn.commit()
    return render_template("message.html", message="Purchase successful!")
    

@app.route("/reset")
def reset():
    initialize_db()
    return render_template("message.html", message="Database reset.")

if __name__ == '__main__':
    initialize_db()
    app.run(debug = True)