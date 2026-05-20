import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("data/groceries.db")

# Grocery
grocery_df = pd.read_sql("""
SELECT store, SUM(amount) as total
FROM grocery_logs
WHERE category='Grocery'
GROUP BY store
ORDER BY total DESC
""", conn)

# Others
other_df = pd.read_sql("""
SELECT store, SUM(amount) as total
FROM grocery_logs
WHERE category!='Grocery'
GROUP BY store
ORDER BY total DESC
""", conn)

fig, axes = plt.subplots(1, 2, figsize=(14,6))

# LEFT = groceries
axes[0].barh(grocery_df["store"],
             grocery_df["total"])

axes[0].set_title("Grocery Stores Spending")
axes[0].set_xlabel("Amount (£)")
axes[0].invert_yaxis()

# RIGHT = others
axes[1].barh(other_df["store"],
             other_df["total"])

axes[1].set_title("Other Spending")
axes[1].set_xlabel("Amount (£)")
axes[1].invert_yaxis()

plt.tight_layout()
plt.show()

conn.close()