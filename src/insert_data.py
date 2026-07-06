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
    ("2026-01-31", "M&S", 4.95, "Grocery"),

# ============================
# February 2026 Spending Data
# ============================

    # WEEK 1
    ("2026-02-02", "M&S", 1.60, "Grocery"),
    ("2026-02-02", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-02-02", "Waitrose", 2.95, "Grocery"),

    ("2026-02-03", "Lidl", 15.89, "Grocery"),

    ("2026-02-05", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-02-05", "Oseyo", 2.19, "Grocery"),
    ("2026-02-05", "M&S", 3.20, "Grocery"),

    ("2026-02-06", "Tesco", 3.85, "Grocery"),

    ("2026-02-07", "TfL", 1.75, "Transport"),
    ("2026-02-07", "Pret", 3.40, "Eating Out"),
    ("2026-02-07", "Potpot Malatang", 26.70, "Eating Out"),
    ("2026-02-07", "Boots", 8.25, "Eating Out"),
    ("2026-02-07", "Lindt", 4.00, "Eating Out"),
    ("2026-02-07", "Meet Fresh", 5.55, "Eating Out"),

    ("2026-02-08", "TfL", 3.50, "Transport"),
    ("2026-02-08", "Paradox Museum", 24.70, "Eating out"),
    ("2026-02-08", "Daphne’s", 22.70, "Eating Out"),

    # WEEK 2
    ("2026-02-09", "M&S", 1.60, "Grocery"),
    ("2026-02-09", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-02-09", "Lidl", 9.19, "Grocery"),

    ("2026-02-10", "TfL", 1.75, "Transport"),
    ("2026-02-10", "Oseyo", 1.98, "Grocery"),
    ("2026-02-10", "Seoul Plaza", 6.26, "Grocery"),
    ("2026-02-10", "McDonald’s", 2.49, "Eating Out"),

    ("2026-02-12", "City Oat Latte", 4.05, "Eating Out"),
    ("2026-02-12", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-02-13", "M&S", 1.60, "Grocery"),
    ("2026-02-13", "Tesco", 3.85, "Grocery"),
    ("2026-02-13", "Lidl", 2.85, "Grocery"),

    ("2026-02-14", "ITSU", 8.75, "Eating Out"),
    ("2026-02-14", "Lidl", 10.04, "Grocery"),
    ("2026-02-14", "M&S", 2.65, "Grocery"),
    ("2026-02-14", "Boots", 9.14, "Eating Out"),

    # WEEK 3
    ("2026-02-16", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-02-16", "Lidl", 4.44, "Grocery"),

    ("2026-02-17", "ITSU", 6.99, "Eating Out"),
    ("2026-02-17", "Sainsbury’s", 8.20, "Grocery"),
    ("2026-02-17", "M&S", 1.60, "Grocery"),

    ("2026-02-19", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-02-19", "M&S", 4.00, "Grocery"),
    ("2026-02-19", "Lidl", 11.19, "Grocery"),

    ("2026-02-20", "M&S", 5.40, "Grocery"),

    ("2026-02-21", "TfL", 3.50, "Transport"),
    ("2026-02-21", "Royal China", 47.54, "Eating Out"),
    ("2026-02-21", "HEYTEA", 5.30, "Eating Out"),
    ("2026-02-21", "Aldi", 3.32, "Grocery"),

    ("2026-02-22", "Lidl", 9.32, "Grocery"),

    # WEEK 4
    ("2026-02-23", "Sainsbury’s", 5.35, "Grocery"),

    ("2026-02-25", "M&S", 1.60, "Grocery"),
    ("2026-02-25", "Tesco", 1.80, "Grocery"),
    ("2026-02-25", "ITSU", 8.75, "Eating Out"),

    ("2026-02-26", "Tesco", 6.15, "Grocery"),

    ("2026-02-27", "Tesco", 3.85, "Grocery"),
    ("2026-02-27", "Waitrose", 4.20, "Grocery"),
    ("2026-02-27", "Lidl", 4.75, "Grocery"),

    ("2026-02-28", "ITSU", 6.99, "Eating Out"),
    ("2026-02-28", "M&S", 1.60, "Grocery"),
    ("2026-02-28", "Lidl", 6.17, "Grocery"),

# ============================
# March 2026 Spending Data
# ============================

    # WEEK 1
    ("2026-03-02", "M&S", 1.60, "Grocery"),
    ("2026-03-02", "Tesco", 3.85, "Grocery"),

    ("2026-03-03", "TfL", 6.10, "Transport"),
    ("2026-03-03", "Bath Bus U2", 5.20, "Transport"),
    ("2026-03-03", "Starbucks", 4.50, "Eating Out"),   # estimate if unknown
    ("2026-03-03", "Roman Bath Ticket", 25.00, "Entertainment"),
    ("2026-03-03", "Bath Lunch", 17.50, "Eating Out"), # estimate if unknown
    ("2026-03-03", "Sally Lunn Bun", 6.50, "Eating Out"),
    ("2026-03-03", "Prior Park Ticket", 12.00, "Entertainment"),
    ("2026-03-03", "M&S", 1.90, "Grocery"),

    ("2026-03-04", "Lidl", 5.42, "Grocery"),

    ("2026-03-05", "M&S", 5.20, "Grocery"),
    ("2026-03-05", "Sainsbury’s", 8.60, "Grocery"),

    ("2026-03-07", "Sainsbury’s", 6.49, "Grocery"),
    ("2026-03-07", "M&S", 3.20, "Grocery"),

    # WEEK 2
    ("2026-03-09", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-03-09", "Lidl", 9.58, "Grocery"),

    ("2026-03-11", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-03-11", "Lidl", 3.28, "Grocery"),

    ("2026-03-12", "City Coffee", 3.45, "Eating Out"),
    ("2026-03-12", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-03-13", "Tesco", 3.85, "Grocery"),
    ("2026-03-13", "Waitrose", 4.75, "Grocery"),

    ("2026-03-14", "TfL", 5.25, "Transport"),
    ("2026-03-14", "LEON", 3.95, "Eating Out"),
    ("2026-03-14", "Ma Eum", 27.27, "Eating Out"),
    ("2026-03-14", "IKEA", 4.75, "Shopping"),
    ("2026-03-14", "Arabica", 5.25, "Eating Out"),
    ("2026-03-14", "Marugame Udon", 11.95, "Eating Out"),
    ("2026-03-14", "Aldi", 3.21, "Grocery"),

    # WEEK 3
    ("2026-03-16", "Sainsbury’s", 6.65, "Grocery"),
    ("2026-03-16", "Lidl", 7.79, "Grocery"),

    ("2026-03-18", "Tesco", 7.70, "Grocery"),
    ("2026-03-18", "Boots", 2.80, "Health"),

    ("2026-03-19", "Tesco", 3.85, "Grocery"),
    ("2026-03-19", "Tesco", 2.50, "Grocery"),
    ("2026-03-19", "Sainsbury’s", 5.65, "Grocery"),
    ("2026-03-19", "Oseyo", 5.19, "Grocery"),

    ("2026-03-20", "M&S", 1.60, "Grocery"),
    ("2026-03-20", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-03-21", "Boots", 10.65, "Health"),
    ("2026-03-21", "Uniqlo", 29.90, "Shopping"),
    ("2026-03-21", "Primark", 6.00, "Shopping"),
    ("2026-03-21", "TfL", 1.75, "Transport"),

    ("2026-03-21", "M&S", 1.60, "Grocery"),
    ("2026-03-21", "M&S", 3.80, "Grocery"),
    ("2026-03-21", "Aldi", 2.83, "Grocery"),

    # WEEK 4
    ("2026-03-23", "M&S", 3.95, "Grocery"),
    ("2026-03-23", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-03-23", "Sainsbury’s", 4.85, "Grocery"),
    ("2026-03-23", "Lidl", 16.95, "Grocery"),

    ("2026-03-26", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-03-26", "Sainsbury’s", 1.65, "Grocery"),
    ("2026-03-26", "Lidl", 5.26, "Grocery"),

    ("2026-03-27", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-03-27", "Aldi", 1.15, "Grocery"),
    ("2026-03-27", "M&S", 3.20, "Grocery"),

    ("2026-03-28", "Lidl", 20.84, "Grocery"),

    ("2026-03-30", "M&S", 1.60, "Grocery"),
    ("2026-03-30", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-03-30", "Sainsbury’s", 1.80, "Grocery"),

    ("2026-03-31", "M&S", 1.60, "Grocery"),
    ("2026-03-31", "Tesco", 7.80, "Grocery"),

# ============================
# April 2026 Spending Data
# ============================

    # WEEK 1
    ("2026-04-02", "City Cafe", 3.45, "Eating Out"),
    ("2026-04-02", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-04-02", "Tesco", 2.50, "Grocery"),

    ("2026-04-03", "Lidl", 16.28, "Grocery"),

    ("2026-04-04", "M&S", 3.45, "Grocery"),
    ("2026-04-04", "TfL", 1.75, "Transport"),
    ("2026-04-04", "Seoul Plaza", 1.69, "Grocery"),
    ("2026-04-04", "Tesco", 3.85, "Grocery"),
    ("2026-04-04", "Primark", 8.00, "Shopping"),

    # WEEK 2
    ("2026-04-06", "M&S", 1.60, "Grocery"),
    ("2026-04-06", "McDonald’s", 2.49, "Eating Out"),
    ("2026-04-06", "Lidl", 0.99, "Grocery"),

    ("2026-04-07", "Sainsbury’s", 9.05, "Grocery"),
    ("2026-04-07", "M&S", 9.75, "Grocery"),

    ("2026-04-08", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-04-09", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-04-09", "Aldi", 3.33, "Grocery"),
    ("2026-04-09", "M&S", 2.65, "Grocery"),

    ("2026-04-10", "City Oat Latte", 4.05, "Eating Out"),
    ("2026-04-10", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-04-10", "Lidl", 13.24, "Grocery"),

    ("2026-04-11", "M&S", 1.60, "Grocery"),
    ("2026-04-11", "ITSU", 9.25, "Eating Out"),

    # WEEK 3
    ("2026-04-13", "Lidl", 9.97, "Grocery"),

    ("2026-04-14", "City Coffee", 3.45, "Eating Out"),
    ("2026-04-14", "Tesco", 3.85, "Grocery"),

    ("2026-04-15", "M&S", 10.55, "Grocery"),
    ("2026-04-15", "Aldi", 2.89, "Grocery"),

    ("2026-04-16", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-04-16", "M&S", 8.00, "Grocery"),

    ("2026-04-17", "Tesco", 3.85, "Grocery"),
    ("2026-04-17", "Lidl", 3.04, "Grocery"),

    ("2026-04-18", "Lidl", 16.71, "Grocery"),

    # WEEK 4
    ("2026-04-20", "ITSU", 9.25, "Eating Out"),
    ("2026-04-20", "Sainsbury’s", 7.10, "Grocery"),

    ("2026-04-21", "Lidl", 12.39, "Grocery"),

    ("2026-04-23", "ITSU", 9.25, "Eating Out"),
    ("2026-04-23", "Aldi", 5.72, "Grocery"),
    ("2026-04-23", "M&S", 2.94, "Grocery"),

    ("2026-04-24", "TfL", 1.75, "Transport"),
    ("2026-04-24", "LEON", 11.84, "Eating Out"),
    ("2026-04-24", "Boots", 14.63, "Health"),
    ("2026-04-24", "Arabica", 5.60, "Eating Out"),
    ("2026-04-24", "Seoul Plaza", 3.48, "Grocery"),
    ("2026-04-24", "M&S", 3.20, "Grocery"),
    ("2026-04-24", "H&M", 12.99, "Shopping"),
    ("2026-04-24", "Primark", 14.00, "Shopping"),

    ("2026-04-25", "Lidl", 13.20, "Grocery"),

    # WEEK 5
    ("2026-04-27", "Tesco", 3.85, "Grocery"),

    ("2026-04-28", "Lidl", 6.74, "Grocery"),

    ("2026-04-29", "Lidl", 5.39, "Grocery"),

    ("2026-04-30", "Aldi", 1.98, "Grocery"),
    ("2026-04-30", "M&S", 5.60, "Grocery"),
    ("2026-04-30", "Tesco", 3.85, "Grocery"),

# ============================
# May 2026 Spending Data
# ============================

    # WEEK 1
    ("2026-05-02", "TfL", 6.50, "Transport"),
    ("2026-05-02", "LEON", 3.95, "Eating Out"),
    ("2026-05-02", "Barang", 52.88, "Shopping"),
    ("2026-05-02", "Boots", 5.93, "Health"),
    ("2026-05-02", "Arabica", 5.60, "Eating Out"),
    ("2026-05-02", "Tesco", 1.65, "Grocery"),
    ("2026-05-02", "M&S", 3.20, "Grocery"),

    ("2026-05-03", "Lidl", 12.01, "Grocery"),

    # WEEK 2
    ("2026-05-04", "ITSU", 9.25, "Eating Out"),
    ("2026-05-04", "Sainsbury’s", 3.95, "Grocery"),

    ("2026-05-05", "Lidl", 12.05, "Grocery"),

    ("2026-05-07", "Lidl", 4.90, "Grocery"),

    ("2026-05-08", "M&S", 8.00, "Grocery"),

    ("2026-05-09", "Sainsbury’s", 14.40, "Grocery"),

    # WEEK 3
    ("2026-05-11", "Lidl", 19.68, "Grocery"),

    ("2026-05-13", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-05-13", "M&S", 4.80, "Grocery"),

    ("2026-05-14", "McDonald’s", 6.89, "Eating Out"),
    ("2026-05-14", "Tesco", 1.25, "Grocery"),

    ("2026-05-15", "ITSU", 9.25, "Eating Out"),
    ("2026-05-15", "Sainsbury’s", 7.25, "Grocery"),
    ("2026-05-15", "Lidl", 9.92, "Grocery"),

    # WEEK 4
    ("2026-05-19", "Lidl", 16.09, "Grocery"),

    ("2026-05-21", "Windsor Castle Ticket", 32.00, "Entertainment"),
    ("2026-05-21", "TfL", 20.60, "Transport"),
    ("2026-05-21", "Boots", 3.20, "Health"),
    ("2026-05-21", "LEON", 4.19, "Eating Out"),
    ("2026-05-21", "M&S", 5.20, "Grocery"),
    ("2026-05-21", "Wasabi", 7.25, "Eating Out"),
    ("2026-05-21", "Windsor Cafe", 4.60, "Eating Out"),
    ("2026-05-21", "GAIL's", 6.50, "Eating Out"),
    ("2026-05-21", "Aldi", 10.00, "Grocery"),

    ("2026-05-23", "Train Ticket", 27.60, "Transport"),
    ("2026-05-23", "TfL", 13.40, "Transport"),
    ("2026-05-23", "Starbucks", 4.65, "Eating Out"),
    ("2026-05-23", "Sainsbury’s", 3.10, "Grocery"),
    ("2026-05-23", "M&S", 2.50, "Grocery"),
    ("2026-05-23", "Independent Cafe", 4.70, "Eating Out"),
    ("2026-05-23", "Brunch", 17.50, "Eating Out"),
    ("2026-05-23", "Devil Wears Prada", 32.00, "Entertainment"),
    ("2026-05-23", "Sephora", 11.04, "Shopping"),
    ("2026-05-23", "Wingstop", 9.95, "Eating Out"),

    ("2026-05-24", "Lidl", 11.84, "Grocery"),

    # WEEK 5
    ("2026-05-25", "TfL", 8.75, "Transport"),
    ("2026-05-25", "Starbucks", 5.00, "Eating Out"),
    ("2026-05-25", "St. James Park Breakfast", 12.40, "Eating Out"),
    ("2026-05-25", "Shake Shack", 5.15, "Eating Out"),
    ("2026-05-25", "Boots", 1.40, "Health"),
    ("2026-05-25", "LEON", 3.90, "Eating Out"),
    ("2026-05-25", "Vietnamese Dinner", 20.00, "Eating Out"),

    ("2026-05-26", "Lidl", 23.67, "Grocery"),

    ("2026-05-27", "Tesco", 7.70, "Grocery"),
    ("2026-05-27", "Boots", 5.40, "Health"),

    ("2026-05-28", "Sainsbury’s", 2.50, "Grocery"),
    ("2026-05-28", "Sainsbury’s", 2.25, "Grocery"),
    ("2026-05-28", "M&S", 1.95, "Grocery"),

    ("2026-05-29", "Lidl", 9.95, "Grocery"),

    ("2026-05-30", "TfL", 3.50, "Transport"),
    ("2026-05-30", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-05-30", "Primark", 11.80, "Shopping"),
    ("2026-05-30", "Oseyo", 5.89, "Grocery"),
    ("2026-05-30", "Molly Tea", 5.50, "Eating Out"),
    ("2026-05-30", "Whole Foods", 9.36, "Grocery"),

    ("2026-05-31", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-05-31", "M&S", 4.80, "Grocery"),
    ("2026-05-31", "McDonald’s", 5.58, "Eating Out"),

# ============================
# June 2026 Spending Data
# ============================

    # WEEK 1
    ("2026-06-01", "TfL", 3.50, "Transport"),
    ("2026-06-01", "Cafe Kitsune", 7.50, "Eating Out"),
    ("2026-06-01", "McDonald’s", 5.08, "Eating Out"),
    ("2026-06-01", "Boots", 2.95, "Health"),
    ("2026-06-01", "Primark", 8.00, "Shopping"),

    ("2026-06-02", "ITSU", 9.25, "Eating Out"),
    ("2026-06-02", "Tesco", 3.85, "Grocery"),

    ("2026-06-03", "Lidl", 13.97, "Grocery"),

    ("2026-06-05", "LEON", 4.00, "Eating Out"),
    ("2026-06-05", "Tesco", 3.85, "Grocery"),

    ("2026-06-06", "Lidl", 12.35, "Grocery"),

    ("2026-06-07", "TfL", 1.75, "Transport"),
    ("2026-06-07", "Jollibee", 9.48, "Eating Out"),
    ("2026-06-07", "Starbucks", 5.00, "Eating Out"),
    ("2026-06-07", "M&S", 4.65, "Grocery"),

    # WEEK 2
    ("2026-06-08", "Lidl", 8.89, "Grocery"),

    ("2026-06-09", "Tesco", 3.85, "Grocery"),
    ("2026-06-09", "ITSU", 8.99, "Eating Out"),

    ("2026-06-10", "M&S", 10.40, "Grocery"),

    ("2026-06-11", "Lidl", 13.83, "Grocery"),

    ("2026-06-12", "McDonald’s", 5.99, "Eating Out"),
    ("2026-06-12", "M&S", 9.00, "Grocery"),

    ("2026-06-13", "Tesco", 3.85, "Grocery"),
    ("2026-06-13", "ITSU", 8.99, "Eating Out"),

    ("2026-06-14", "TfL", 3.50, "Transport"),
    ("2026-06-14", "Cay Tre", 21.55, "Eating Out"),
    ("2026-06-14", "Starbucks", 6.15, "Eating Out"),
    ("2026-06-14", "Tesco", 4.40, "Grocery"),
    ("2026-06-14", "Boots", 2.00, "Health"),

    # WEEK 3
    ("2026-06-15", "Lidl", 12.93, "Grocery"),

    ("2026-06-16", "Sainsbury’s", 3.95, "Grocery"),
    ("2026-06-16", "ITSU", 9.25, "Eating Out"),
    ("2026-06-16", "Starbucks", 6.00, "Eating Out"),

    ("2026-06-17", "Sainsbury’s", 4.85, "Grocery"),
    ("2026-06-17", "Sainsbury’s", 1.95, "Grocery"),
    ("2026-06-17", "Sainsbury’s", 2.25, "Grocery"),
    ("2026-06-17", "Boots", 6.90, "Health"),
    ("2026-06-17", "M&S", 10.85, "Grocery"),
    ("2026-06-17", "Lidl", 3.76, "Grocery"),

    ("2026-06-18", "Lidl", 16.00, "Grocery"),

    ("2026-06-19", "TfL", 3.50, "Transport"),
    ("2026-06-19", "M&S", 40.45, "Grocery"),
    ("2026-06-19", "Whittard", 27.80, "Shopping"),
    ("2026-06-19", "Seoul Plaza", 8.46, "Grocery"),
    ("2026-06-19", "Boots", 1.80, "Health"),
    ("2026-06-19", "Sainsbury’s", 1.65, "Grocery"),
    ("2026-06-19", "LEON", 11.49, "Eating Out"),

    ("2026-06-20", "TfL", 3.50, "Transport"),
    ("2026-06-20", "JOE & JUICE", 17.30, "Eating Out"),
    ("2026-06-20", "Fortnum & Mason", 14.20, "Shopping"),
    ("2026-06-20", "Boots", 7.75, "Health"),
    ("2026-06-20", "London Gift", 8.97, "Shopping"),
    ("2026-06-20", "M&S", 11.35, "Grocery"),
    ("2026-06-20", "Starbucks", 6.15, "Eating Out"),
    ("2026-06-20", "Aldi", 3.17, "Grocery"),

    ("2026-06-21", "Lidl", 16.04, "Grocery")

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
print("February 2026 Groceries Data Inserted Successfully")
print("March 2026 Groceries Data Inserted Successfully")
print("April 2026 Groceries Data Inserted Successfully")
print("May 2026 Groceries Data Inserted Successfully")
print("June 2026 Groceries Data Inserted Successfully")