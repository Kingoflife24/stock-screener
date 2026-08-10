# S&P 500 Stock Screener

A Python-based stock screener that filters S&P 500 companies by sector, market cap, and other fundamentals. Built on top of an existing MySQL database of company data, with a command-line interface for flexible querying.

## Features
- Pulls company fundamentals (sector, market cap, revenue growth) from a MySQL database
- Composable filter functions (sector, market cap) chainable with AND logic
- CLI interface via `argparse` for querying without editing code
- Live data fetch supplement via `yfinance` for real-time PE ratios

## Tech Stack
- Python 3
- MySQL (mysql-connector-python)
- yfinance
- argparse

## Setup
1. Clone the repo
```bash
   git clone https://github.com/Kingoflife24/stock-screener.git
   cd stock-screener
```
2. Create a virtual environment and install dependencies
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
```
3. Set up your `.env` file with your MySQL password

4. Ensure your MySQL database `sp500_companies` with table `companies` is populated (see [sp500-sql project](https://github.com/Kingoflife24/sp500-sql) for schema)

## Usage
```bash
python main.py --sector Technology --min-cap 500000000000
```

**Example output:**

## Roadmap
- [ ] Expand dataset to full S&P 500 (~500 companies)
- [ ] Add PE ratio and revenue growth filters
- [ ] Add scoring/ranking system
- [ ] Add pytest test coverage