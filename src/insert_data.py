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

# ============================
# January 2026 Spending Data
# ============================

    # WEEK ONE
    ("2026-01-01", "Lidl", 9.58, "Grocery"),

    ("2026-01-02", "Aldi", 4.15, "Grocery"),
    ("2026-01-02", "Tesco", 3.85, "Grocery"),
    ("2026-01-02", "Lidl", 4.85, "Grocery"),

    ("2026-01-05", "Lidl", 13.11, "Grocery"),

    ("2026-01-07", "Tesco", 4.90, "Grocery"),
    ("2026-01-07", "Lidl", 3.83, "Grocery"),

    ("2026-01-09", "Oseyo", 2.99, "Grocery"),
    ("2026-01-09", "Waitrose", 3.55, "Grocery"),
    ("2026-01-09", "Tesco", 3.85, "Grocery"),

    ("2026-01-10", "Aldi", 10.79, "Grocery"),

    # WEEK TWO
    ("2026-01-12", "Sainsbury’s", 5.15, "Grocery"),
    ("2026-01-12", "M&S", 4.80, "Grocery"),
    ("2026-01-12", "Lidl", 7.29, "Grocery"),

    ("2026-01-14", "Lidl", 11.49, "Grocery"),

    ("2026-01-15", "Tesco", 7.25, "Grocery"),
    ("2026-01-15", "Lidl", 0.35, "Grocery"),

    # WEEK THREE
    ("2026-01-19", "Lidl", 11.82, "Grocery"),

    ("2026-01-21", "Lidl", 12.64, "Grocery"),

    ("2026-01-23", "Greggs", 3.35, "Eating Out"),
    ("2026-01-23", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-01-24", "M&S", 1.65, "Grocery"),
    ("2026-01-24", "Lidl", 6.77, "Grocery"),

    # WEEK FOUR
    ("2026-01-26", "M&S", 3.55, "Grocery"),
    ("2026-01-26", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-01-27", "ITSU", 6.99, "Eating Out"),
    ("2026-01-27", "Tesco", 5.75, "Grocery"),
    ("2026-01-27", "Lidl", 5.15, "Grocery"),

    ("2026-01-29", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-01-29", "Lidl", 4.33, "Grocery"),

    ("2026-01-30", "McDonald’s", 4.58, "Eating Out"),
    ("2026-01-30", "M&S", 1.60, "Grocery"),

    ("2026-01-31", "Oseyo", 3.38, "Grocery"),
    ("2026-01-31", "Tesco", 5.05, "Grocery"),
    ("2026-01-31", "M&S", 4.95, "Grocery")

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
print("January 2026 Groceries Data Inserted Successfully")