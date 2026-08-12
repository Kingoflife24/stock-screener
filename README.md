# S&P 500 Stock Screener

A Python-based stock screener that filters S&P 500 companies by sector, market cap, PE ratio, and revenue growth. Built on a MySQL database of company fundamentals for all 503 S&P 500 constituents, with a command-line interface for flexible querying.

## Features
- Full S&P 500 dataset (503 companies) stored in MySQL, pulled via `yfinance`
- Composable filter functions (sector, market cap, PE ratio, revenue growth) chainable with AND logic
- CLI interface via `argparse` for querying without editing code
- Upsert-based data population script — safe to re-run to refresh fundamentals

## Tech Stack
- Python 3
- MySQL (mysql-connector-python)
- yfinance
- pandas
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

4. Create the `companies` table in a `sp500_companies` MySQL database, then populate it:

```bash
python populate_db.py
```

This pulls the current S&P 500 ticker list from Wikipedia and fetches fundamentals for each via `yfinance`. Takes a few minutes on first run.

## Usage

```bash
python main.py --sector Technology --max-pe 25 --min-growth 0.1
```

**Available filters:**

| Flag | Description | Example |
|---|---|---|
| `--sector` | Filter by GICS sector | `Technology` |
| `--min-cap` | Minimum market cap | `500000000000` |
| `--max-pe` | Maximum PE ratio | `25` |
| `--min-growth` | Minimum revenue growth (decimal) | `0.1` (10%) |

**Example output:**

## Roadmap

- [ ] Add scoring/ranking system to weight multiple factors
- [ ] Add pytest test coverage for filter functions
- [ ] Optional: simple Streamlit front-end