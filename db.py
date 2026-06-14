import sqlite3

def get_conn():
    return sqlite3.connect("spending.db")

def init_db():
    with get_conn() as conn:
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS expenses (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     category TEXT NOT NULL,
                     amount REAL NOT NULL,
                     note TEXT,
                     date TEXT DEFAULT (DATE('now'))
                     )
                     """)
        
        conn.execute("""
                     CREATE TABLE IF NOT EXISTS budgets (
                     category TEXT PRIMARY KEY,
                     amount REAL NOT NULL
                     )
                     """)

def add_expense(category, amount, note=None):
    with get_conn() as conn:
        conn.execute("INSERT INTO expenses (category, amount, note) VALUES (?, ?, ?)", (category.lower(), amount, note))

def get_expenses(period="month"):
    filter_sql = "WHERE date >= DATE('now', 'start of month')" if period == "month" else ""
    with get_conn() as conn:
        return conn.execute(
            f"SELECT category, amount, note, date FROM expenses {filter_sql} ORDER BY date DESC"
        ).fetchall()
    
def get_summary(period="month"):
    with get_conn() as conn:
        return conn.execute("""
                            SELECT category, SUM(amount) as total
                            FROM expenses
                            WHERE date >= DATE('now', 'start of month')
                            GROUP BY category
                            ORDER BY total DESC
                            """).fetchall()

def set_budget(category, amount):
    with get_conn() as conn:
        conn.execute("INSERT OR REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category.lower(), amount))

def get_budgets():
    with get_conn() as conn:
        return conn.execute("SELECT category, amount FROM budgets").fetchall()