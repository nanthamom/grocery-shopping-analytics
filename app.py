import sqlite3
import streamlit as st
import pandas as pd

# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Grocery Shopping Analytics",
    page_icon="🛒",
    layout="wide"
)

# -----------------------------
# Database connection
# -----------------------------

conn = sqlite3.connect("data/groceries.db")

# -----------------------------
# Load data
# -----------------------------

df = pd.read_sql(
    "SELECT * FROM grocery_logs",
    conn
)

conn.close()

# -----------------------------
# Dashboard title
# -----------------------------

st.title("🛒 Grocery Shopping Analytics")
st.subheader("London Student Edition")

st.write(
    "An interactive dashboard analysing my personal spending "
    "using Python, SQLite, SQL and Pandas."
)

total_spending = df["amount"].sum()
average_transaction = df["amount"].mean()
number_of_transactions = len(df)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Spending",
    f"£{total_spending:,.2f}"
)

col2.metric(
    "Average Transaction",
    f"£{average_transaction:,.2f}"
)

col3.metric(
    "Transactions",
    number_of_transactions
)

monthly_df = pd.read_sql(
    """
    SELECT
        strftime('%Y-%m', date) AS month,
        SUM(amount) AS total
    FROM grocery_logs
    GROUP BY month
    ORDER BY month
    """,
    sqlite3.connect("data/groceries.db")
)

st.subheader("📈 Monthly Spending")

st.bar_chart(
    monthly_df.set_index("month")
)

# -----------------------------
# Basic information
# -----------------------------

st.write("### Transaction Data")

st.dataframe(df)