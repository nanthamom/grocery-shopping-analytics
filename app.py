import sqlite3
import streamlit as st
import pandas as pd

# ---------------------------------
# Page configuration
# ---------------------------------

st.set_page_config(
    page_title="Grocery Shopping Analytics",
    page_icon="🛒",
    layout="wide"
)

# ---------------------------------
# Load database
# ---------------------------------

conn = sqlite3.connect("data/groceries.db")

df = pd.read_sql(
    "SELECT * FROM grocery_logs",
    conn
)

conn.close()

# Convert date to datetime
df["date"] = pd.to_datetime(df["date"])

# ---------------------------------
# Dashboard title
# ---------------------------------

st.title("NANTHA & LITTLE BITS BOBS")
st.subheader("Grocery Shopping Analytics - London Student Edition")

st.write(
    "An interactive dashboard analysing my personal spending "
    "using Python, SQLite, SQL and Pandas."
)

# ---------------------------------
# Sidebar filters
# ---------------------------------

st.sidebar.header("Filters")

# Month filter
df["month"] = df["date"].dt.strftime("%Y-%m")

months = sorted(df["month"].unique())

selected_months = st.sidebar.multiselect(
    "Month",
    options=months,
    default=months
)

# Category filter
categories = sorted(df["category"].unique())

selected_categories = st.sidebar.multiselect(
    "Category",
    options=categories,
    default=categories
)

# Store filter
stores = sorted(df["store"].unique())

selected_stores = st.sidebar.multiselect(
    "Store",
    options=stores,
    default=stores
)

# ---------------------------------
# Apply filters
# ---------------------------------

filtered_df = df[
    (df["month"].isin(selected_months)) &
    (df["category"].isin(selected_categories)) &
    (df["store"].isin(selected_stores))
]

# ---------------------------------
# KPI calculations
# ---------------------------------

total_spending = filtered_df["amount"].sum()

average_transaction = (
    filtered_df["amount"].mean()
    if len(filtered_df) > 0
    else 0
)

number_of_transactions = len(filtered_df)

# ---------------------------------
# KPI cards
# ---------------------------------

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

# ---------------------------------
# Monthly Spending
# ---------------------------------

st.header("Monthly Spending")

monthly_df = (
    filtered_df
    .groupby("month")["amount"]
    .sum()
    .reset_index()
)

monthly_df = monthly_df.sort_values("month")

st.bar_chart(
    monthly_df.set_index("month")
)

# ---------------------------------
# Grocery vs Other Spending
# ---------------------------------

st.header("Grocery vs Other Spending")

grocery_total = filtered_df[
    filtered_df["category"] == "Grocery"
]["amount"].sum()

other_total = filtered_df[
    filtered_df["category"] != "Grocery"
]["amount"].sum()

col1, col2 = st.columns(2)

col1.metric(
    "🛒 Grocery Spending",
    f"£{grocery_total:,.2f}"
)

col2.metric(
    "☕ Other Spending",
    f"£{other_total:,.2f}"
)

# ---------------------------------
# Grocery vs Other chart
# ---------------------------------

comparison_df = pd.DataFrame({
    "Type": ["Grocery", "Other"],
    "Amount": [grocery_total, other_total]
})

st.bar_chart(
    comparison_df.set_index("Type")
)

# ---------------------------------
# Store-level analysis
# ---------------------------------

col1, col2 = st.columns(2)

# Grocery stores
with col1:

    st.subheader("Grocery Stores")

    grocery_df = (
        filtered_df[
            filtered_df["category"] == "Grocery"
        ]
        .groupby("store")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    if len(grocery_df) > 0:
        st.bar_chart(grocery_df)
    else:
        st.info("No grocery spending for the selected filters.")


# Other spending
with col2:

    st.subheader("Other Spending")

    other_df = (
        filtered_df[
            filtered_df["category"] != "Grocery"
        ]
        .groupby("store")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    if len(other_df) > 0:
        st.bar_chart(other_df)
    else:
        st.info("No other spending for the selected filters.")

# ---------------------------------
# Transaction Data
# ---------------------------------

st.header("Transaction Data")

display_df = filtered_df[
    ["date", "store", "amount", "category"]
].sort_values("date", ascending=False)

st.dataframe(
    display_df,
    use_container_width=True
)
