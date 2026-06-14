# Spending Snapshot

A lightweight terminal based expense tracker built with Python and SQLite. Log purchases, set category budgets, and view montly summaries.

## Features

- Add Expense - Log purchase with category, amount and optional note
- Set Budgets - Define spending limits by category
- List Expenses - View all expenses for the current month with details
- Show Summary - See total spending grouped by category
- Persistent Storage - All data saved locally in **spending.db** via SQLite

## Project Structure

- main.py - CLI menu loop and user interaction
- db.py - SQLite database operations
- helpers.py - Input validation utilities

## Requirements

python 3.10+

## Usage

python main.py

## Menu Options

1. Add a new expense
2. Set a budget for a category
3. List this month's expenses
4. Show spending summary by category
0. Exit the application

## Database Schema

### Expenses Table

- id INTEGER - Primary key
- category TEXT - Purchase category
- amount REAL - Amount spent
- note TEXT - Optional note
- date TEXT - Date of entry (Default: today)


### Budgets Table

- category TEXT - Primary key
- amount REAL - Budget limit

## Notes

- All categories are stored in lower case for consistency
- Expense listing and summary default to the current month
- All data is stored in **spending.db** between sessions