import sqlite3
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askopenfilenames # pop open file choice
from os.path import exists # Check if file exists

db_exists = exists(r"C:\Users\Sarmen\PycharmProjects\HelloWorld1\2022_Programming\backAtIt\HackerRank2022\Day54(ShopifyImageRepository)\SQLite_Python.db")

# Prevent redundant table creation
if not db_exists:
    # Create initial table
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    cursor.execute('''CREATE TABLE new_employee
                    ( id INTEGER PRIMARY KEY, name TEXT NOT NULL, photo BLOB NOT NULL);''')
    sqliteConnection.commit()



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
                                  (id, name, photo) VALUES (?, ?, ?)"""
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


# # Initial insert test
# insertBLOB(1, "Smith", r"C:\Users\Sarmen\PycharmProjects\HelloWorld1\2022_Programming\backAtIt\HackerRank2022\Day54(ShopifyImageRepository)\pexels-chevanon-photography-1108099.jpg")

# Custom photo insert test (as many photos as you want)
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
filename = askopenfilenames(title='Choose a photo to upload')
print(filename)

# # Adding photos from selected photos on previous action
# for count, file in enumerate(filename):
#     insertBLOB(count,'Ally', file)


sqliteConnection = sqlite3.connect('SQLite_Python.db')
cursor = sqliteConnection.cursor()
cursor.execute("SELECT id FROM new_employee ORDER BY id DESC LIMIT 1")
finalEntryID = cursor.fetchone()
print(finalEntryID)
sqliteConnection.close()

# Adding photos from selected photos on previous action
for count, file in enumerate(filename):
    insertBLOB(count + finalEntryID[0], 'Ally', file)

# Initial read from DB and write to DISK test
readBlobData(26)

"""NEED CLICK INPUTS FOR WEB SERVER WHICH ALLOWS SEARCH VIA TYPED COMMAND AND INPUTTING OF IMAGES VIA UPLOAD BUTTON AND """