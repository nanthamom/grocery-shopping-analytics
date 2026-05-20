# Grocery Shopping Analytics (London Student Edition)

- A Personal Data Analytics Project Using **Python + SQLite + SQL + Matplotlib** to Track and Analyse My Real Monthly Grocery Spending in London.

- This Project Transform My Weekly Google Docs Spending Recordings into a Structured Database and Visual Insights.

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
- Monthly SPending Tracking
- Bar Chart Visualisation Using Matplotlib

# Technologies Used

- Python 3
- SQLite 
- SQL (GROUP, BY, SUM, ORDER BY)
- Matplotlib

# How To Run 

# 1. Create Database
python3 src/create_db.py

# 2. Insert Data 
python3 src/insert_data.py

# 3. Run Analysis
python3 src/analysis.py

# CURRENT OUTPUT (BY 13th Mar 2026)

Database Created Successfully
November 2025 Groceries Data Inserted Successfully
December 2025 Groceries Data Inserted Successfully
January 2026 Groceries Data Inserted Successfully
Total Monthly Grocery Spending 488.23 £

Grocery Spending by Grocery Stores:
Lidl - 234.34 £
M&S - 56.38 £
Sainsbury’s - 49.72 £
Aldi - 41.4 £
Tesco - 34.5 £
EE Mobile - 18.48 £
McDonald’s - 17.76 £
Oseyo - 15.43 £
ITSU - 6.99 £
Waitrose - 5.1 £
Whole Foods - 4.78 £
Greggs - 3.35 £

Monthly spending:
2025-11 - 143.03 £
2025-12 - 150.01 £
2026-01 - 195.19 £

# CURRENT OUTPUT (Updated: 3:53AM - Wednesday, 20th May 2026)

```bash
November 2025 Spending Data Inserted Successfully
December 2025 Spending Data Inserted Successfully
January 2026 Spending Data Inserted Successfully
February 2026 Spending Data Inserted Successfully
March 2026 Spending Data Inserted Successfully
April 2026 Spending Data Inserted Successfully
```

## Total Spending = £1608.26 

## Spending by Store

| Store | Total (£) |
|------|------:|
| Lidl | 475.25 |
| Sainsbury’s | 190.16 |
| M&S | 159.82 |
| Tesco | 105.30 |
| ITSU | 66.22 |
| Aldi | 65.83 |
| Royal China | 47.54 |
| Boots | 45.47 |
| Uniqlo | 29.90 |
| Primark | 28.00 |
| Ma Eum | 27.27 |
| TfL | 27.10 |
| Potpot Malatang | 26.70 |
| Roman Bath Ticket | 25.00 |
| Oseyo | 24.79 |
| Paradox Museum | 24.70 |
| McDonald’s | 22.74 |
| Daphne’s | 22.70 |
| EE Mobile | 18.48 |

## Monthly Spending Trend

| Month | Spending (£) |
|------|------:|
| 2025-11 | 143.03 |
| 2025-12 | 150.01 |
| 2026-01 | 195.19 |
| 2026-02 | 382.14 |
| 2026-03 | 402.11 |
| 2026-04 | 335.78 |

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
- [ ] Add spending visualisations (Matplotlib)
- [ ] Build Streamlit dashboard
- [ ] Predict monthly spending using Python
- [ ] Categorise expenses automatically