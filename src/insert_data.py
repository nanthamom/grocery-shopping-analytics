import sqlite3

# connect to the same database
conn = sqlite3.connect("data/groceries.db")
cursor = conn.cursor()

data = [

# ============================
# November 2025 Groceries Data
# ============================
    
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

# ============================
# December 2025 Groceries Data
# ============================

    # WEEK 1
    ("2025-12-01", "M&S", 1.60, "Grocery"),
    ("2025-12-02", "Aldi", 7.78, "Grocery"),
    ("2025-12-02", "M&S", 6.18, "Grocery"),
    ("2025-12-02", "Lidl", 6.20, "Grocery"),
    ("2025-12-05", "Oseyo", 6.07, "Grocery"),
    ("2025-12-05", "Waitrose", 1.55, "Grocery"),
    ("2025-12-05", "M&S", 7.35, "Grocery"),
    ("2025-12-05", "Lidl", 13.92, "Grocery"),

    # WEEK 2
    ("2025-12-08", "Lidl", 5.87, "Grocery"),
    ("2025-12-09", "Lidl", 9.84, "Grocery"),
    ("2025-12-11", "Sainsbury’s", 3.95, "Grocery"),
    ("2025-12-12", "Lidl", 4.62, "Grocery"),
    ("2025-12-13", "Tesco", 3.85, "Grocery"),
    ("2025-12-14", "McDonald’s", 10.49, "Eating Out"),

    # WEEK 3
    ("2025-12-15", "Sainsbury’s", 6.20, "Grocery"),
    ("2025-12-15", "Sainsbury’s", 1.55, "Grocery"),
    ("2025-12-15", "M&S", 2.96, "Grocery"),
    ("2025-12-15", "Lidl", 5.97, "Grocery"),
    ("2025-12-17", "Lidl", 4.70, "Grocery"),
    ("2025-12-17", "McDonald’s", 2.69, "Eating Out"),

    # WEEK 4
    ("2025-12-23", "Lidl", 7.61, "Grocery"),
    ("2025-12-24", "M&S", 3.81, "Grocery"),
    ("2025-12-24", "Aldi", 6.97, "Grocery"),
    ("2025-12-26", "Lidl", 13.34, "Grocery"),
    ("2025-12-29", "Sainsbury’s", 4.94, "Grocery"),

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
print("December 2025 Groceries Data Inserted Successfully")