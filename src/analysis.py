import sqlite3
import matplotlib.pyplot as plt

# Connect Database 
conn = sqlite3.connect("data/groceries.db")
cursor = conn.cursor()

# ================================
# 1. TOTAL MONTLY GROCERY SPENDING
# ================================
cursor.execute("SELECT SUM(amount) FROM grocery_logs")
total = cursor.fetchone()[0]

print("Total Monthly Grocery Spending", round(total, 2), "£")

# ============================
# 2. SPENDING BY GROCERY STORE
# ============================
cursor.execute("""
SELECT store, SUM(amount)
FROM grocery_logs
GROUP BY store
ORDER BY SUM(amount) DESC
""")

store_results = cursor.fetchall()

print("\nGrocery Spending by Grocery Stores:")
for row in store_results:
    print (row[0], "-", round(row[1], 2), "£")

# ===============================
# 4. MONTHLY TREND
# ===============================
cursor.execute("""
SELECT strftime('%Y-%m', date), SUM(amount)
FROM grocery_logs
GROUP BY strftime('%Y-%m', date)
ORDER BY strftime('%Y-%m', date)
""")

monthly_results = cursor.fetchall()

print("\nMonthly spending:")
for row in monthly_results:
    print(row[0], "-", round(row[1], 2), "£")

# ===============================
# 5. VISUALISATION (BAR CHART)
# ===============================

stores = [row[0] for row in store_results]
amounts = [row[1] for row in store_results]

plt.bar(stores, amounts)
plt.xticks(rotation=45)
plt.title("Spending by Store")
plt.xlabel("Store")
plt.ylabel("Amount (£)")
plt.tight_layout()

plt.show()

# close connection
conn.close()