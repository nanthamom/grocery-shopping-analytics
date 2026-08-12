from sklearn.linear_model import LinearRegression
import sqlite3
import pandas as pd

# ---------------------------------
# Connect to database
# ---------------------------------

conn = sqlite3.connect("data/groceries.db")

# ---------------------------------
# Get monthly grocery spending
# ---------------------------------

query = """
SELECT
    strftime('%Y-%m', date) AS month,
    SUM(amount) AS grocery_spending
FROM grocery_logs
WHERE category = 'Grocery'
GROUP BY strftime('%Y-%m', date)
ORDER BY month;
"""

monthly_df = pd.read_sql(query, conn)

conn.close()

# ---------------------------------
# Display monthly spending
# ---------------------------------

print("\nMonthly Grocery Spending:")
print(monthly_df)

# ---------------------------------
# 3-month moving average
# ---------------------------------

monthly_df["moving_average"] = (
    monthly_df["grocery_spending"]
    .rolling(window=3)
    .mean()
)

# ---------------------------------
# Predict next month
# ---------------------------------

last_three_months = monthly_df["grocery_spending"].tail(3)

prediction = last_three_months.mean()

next_month = (
    pd.Period(
        monthly_df["month"].iloc[-1],
        freq="M"
    ) + 1
)

# ---------------------------------
# Display prediction
# ---------------------------------

print("\nGrocery Spending Forecast")
print("-------------------------")
print(f"Next month: {next_month}")
print(f"Predicted spending: £{prediction:.2f}")

# ---------------------------------
# Linear Regression
# ---------------------------------

monthly_df["month_number"] = range(1, len(monthly_df) + 1)

X = monthly_df[["month_number"]]
y = monthly_df["grocery_spending"]

model = LinearRegression()

model.fit(X, y)

next_month_number = len(monthly_df) + 1

next_month_df = pd.DataFrame({
    "month_number": [next_month_number]
})

linear_prediction = model.predict(
    next_month_df
)[0]

print("\nLinear Regression Forecast")
print("--------------------------")
print(f"Next month: {next_month}")
print(f"Predicted spending: £{linear_prediction:.2f}")