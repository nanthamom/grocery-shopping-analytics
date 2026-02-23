import sqlite3

# connect to the same database
conn = sqlite3.connect("data/groceries.db")
cursor = conn.cursor()

# ============================
# November 2025 Groceries Data
# ============================

data = [
    # WEEK ONE
    ("2025-11-03", "Lidl", 10.07, "Grocery"),
    ("2025-11-03", "M&S", 3.70, "Grocery"),
    ("2025-11-03", "Whole Foods", 4.78, "Grocery"),
    ("2025-11-03", "Aldi", 3.74, "Grocery"),
    ("2025-11-03", "EE Mobile", 18.48, "Bills"),

    ("2025-11-05", "Sainsbury’s", 8.63, "Grocery"),
    ("2025-11-07", "Lidl", 7.38, "Grocery"),
    ("2025-11-08", "M&S", 3.20, "Grocery"),
    ("2025-11-08", "Oseyo", 2.99, "Grocery"),

    # WEEK 2
    ("2025-11-10", "Aldi", 1.43, "Grocery"),
    ("2025-11-11", "Lidl", 5.38, "Grocery"),
    ("2025-11-13", "Lidl", 6.76, "Grocery"),
    ("2025-11-14", "Sainsbury’s", 3.95, "Grocery"),
    ("2025-11-14", "Aldi", 3.45, "Grocery"),
    ("2025-11-14", "M&S", 7.43, "Grocery"),

    # WEEK 3
    ("2025-11-17", "Lidl", 5.39, "Grocery"),
    ("2025-11-18", "Sainsbury’s", 1.60, "Grocery"),
    ("2025-11-18", "Lidl", 3.95, "Grocery"),
    ("2025-11-21", "Sainsbury’s", 1.90, "Grocery"),
    ("2025-11-21", "Lidl", 9.57, "Grocery"),

    # WEEK 4
    ("2025-11-24", "Aldi", 3.09, "Grocery"),
    ("2025-11-24", "M&S", 3.60, "Grocery"),
    ("2025-11-25", "Lidl", 10.02, "Grocery"),
    ("2025-11-28", "Lidl", 12.54, "Grocery"),
]

# Insert all Rows into the Database
cursor.executemany ("""
INSERT INTO grocery_logs (date, store, amount, category)
VALUES (?, ?, ?, ?)""", data)

# Save Changes
conn.commit()
# Close Connection
conn.close()

print("November 2025 Groceries Data Inserted Successfully")