import sqlite3 # Python talk to a SQLite Database
import os # Python interact with files, folders


# ensure data folder exists
os.makedirs("data", exist_ok=True)

# connect to database file
conn = sqlite3.connect("data/groceries.db")
# cursor a remote control to send SQL Commands to the Database
cursor = conn.cursor()

# create table to store grocery purchase records
cursor.execute("""
CREATE TABLE IF NOT EXISTS grocery_logs (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEXT,
               store TEXT,
               amount REAL,
               category TEXT
)
""")

# save changes, without "conn.commit" the table might not be saved
conn.commit()
# close connection
conn.close() 

print("Database Created Successfully")