import sqlite3
import matplotlib.pyplot as plt

# Connect Database 
conn = sqlite3.connect("data/groceries.db")
cursor = conn.cursor()

# ================================
# 1. TOTAL MONTHLY GROCERY SPENDING
# ================================
cursor.execute("SELECT SUM(amount) FROM grocery_logs")
total = cursor.fetchone()[0]

print("Total Grocery Spending:", round(total, 2), "£")

# ============================
# 2. SPENDING BY STORE
# ============================
cursor.execute("""
SELECT store, SUM(amount)
FROM grocery_logs
GROUP BY store
ORDER BY SUM(amount) DESC
""")

store_results = cursor.fetchall()

print("\nSpending by Store:")
for row in store_results:
    print(row[0], "-", round(row[1], 2), "£")

# ===============================
# 3. MONTHLY TREND
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
# 4. VISUALISATION (CLEAN VERSION)
# ===============================

# Only show top 10 stores
top_n = 10
top_results = store_results[:top_n]

stores = [row[0] for row in top_results]
amounts = [row[1] for row in top_results]

plt.figure()
plt.barh(stores, amounts)

plt.title("Top 10 Stores by Spending")
plt.xlabel("Amount (£)")
plt.ylabel("Store")

plt.tight_layout()
plt.show()

# Close connection
conn.close()