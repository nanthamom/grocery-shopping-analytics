# Grocery Shopping Analytics (London Student Edition)

- A Personal Data Analytics Project Using **Python + SQLite + SQL + Matplotlib** to Track and Analyse My Real Monthly Grocery Spending in London.

- This Project Transform My Weekly Google Docs Spending Recordings into a Structured Database and Visual Insights.

## Why I Built This

Instead of using a public dataset, I wanted to analyse my own spending habits as a university student living in London.

The project helped me practice:

- SQL querying
- Database design
- Data cleaning
- Data visualisation
- Python programming

while generating insights from real-world personal finance data.

# Project Overview 

As a University Student in London, I Tracked My Grocery and Food Spending Over Multiple Months.

This Project Turns Raw Data Into: 
- A Structured **SQLite Database**
- SQL Queries for Analysis
- Python Scripts for Insights and Visualisations 

# Features 

- SQLite Database Storing all Transactions
- Categorised Spending (Grocery, Bills, Eating Out)
- Store-Based Analysis (Lidl, Tesco, M&S, etc.)
- Monthly Spending Tracking
- Bar Chart Visualisation Using Matplotlib

# Technologies Used

- Python 3
- SQLite 
- SQL (GROUP, BY, SUM, ORDER BY)
- Matplotlib

# How To Run 

# 0. Delete the SQLite database & Rebuild Python Data
rm data/groceries.db

# 1. Create Database
python3 src/create_db.py

# 2. Insert Data 
python3 src/insert_data.py

# 3. Run Analysis
python3 src/analysis.py

# 4. Run Streamlit
streamlit run app.py

# CURRENT OUTPUT (Updated: 9:30AM - Tuesday, 11th August 2026)

```bash
November 2025 Spending Data Inserted Successfully
December 2025 Spending Data Inserted Successfully
January 2026 Spending Data Inserted Successfully
February 2026 Spending Data Inserted Successfully
March 2026 Spending Data Inserted Successfully
April 2026 Spending Data Inserted Successfully
May 2026 Spending Data Inserted Successfully
June 2026 Spending Data Inserted Successfully
```

## Total Spending = £2696.62

## Spending by Store

## Top 5 Spending Locations

| Store | Total (£) |
|------|------:|
| Lidl | 595.36 |
| Sainsbury's | 234.01 |
| M&S | 190.27 |
| Tesco | 115.90 |
| ITSU | 84.72 |

## Monthly Spending Trend

| Month | Spending (£) |
|------|------:|
| 2025-11 | 143.03 |
| 2025-12 | 150.01 |
| 2026-01 | 195.19 |
| 2026-02 | 382.14 |
| 2026-03 | 402.11 |
| 2026-04 | 335.78 |
| 2026-05 | 619.52 |
| 2026-06 | 468.84 |

---

## Example SQL Queries Used

Total spending:

```sql
SELECT SUM(amount)
FROM grocery_logs;
```

Monthly spending:

```sql
SELECT strftime('%Y-%m', date),
       SUM(amount)
FROM grocery_logs
GROUP BY strftime('%Y-%m', date);
```

Highest spending stores:

```sql
SELECT store,
       SUM(amount)
FROM grocery_logs
GROUP BY store
ORDER BY SUM(amount) DESC;
```
### Future Improvements
- [x] Add spending visualisations (Matplotlib)
- [x] Build Streamlit dashboard
- [x] Add interactive filters
- [x] Add Grocery vs Other Spending analysis
- [ ] Predict monthly spending using Python
- [ ] Categorise expenses automatically