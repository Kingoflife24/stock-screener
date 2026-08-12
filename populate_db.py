import yfinance as yf
import mysql.connector
import os
import time
from dotenv import load_dotenv
from get_tickers import get_sp500_tickers

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="sp500_companies"
    )

def fetch_fundamentals(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return {
        "Exchange": info.get("exchange"),
        "Symbol": symbol,
        "Shortname": info.get("shortName"),
        "Longname": info.get("longName"),
        "Sector": info.get("sector"),
        "Industry": info.get("industry"),
        "Currentprice": info.get("currentPrice"),
        "Marketcap": info.get("marketCap"),
        "Ebitda": info.get("ebitda"),
        "Revenuegrowth": info.get("revenueGrowth"),
        "City": info.get("city"),
        "State": info.get("state"),
        "Country": info.get("country"),
        "Fulltimeemployees": info.get("fullTimeEmployees"),
        "Longbusinesssummary": info.get("longBusinessSummary"),
    }

def upsert_company(conn, data):
    cursor = conn.cursor()
    columns = ", ".join(data.keys())
    placeholders = ", ".join(["%s"] * len(data))
    updates = ", ".join([f"{k}=VALUES({k})" for k in data.keys() if k != "Symbol"])
    sql = f"""
        INSERT INTO companies ({columns}) VALUES ({placeholders})
        ON DUPLICATE KEY UPDATE {updates}
    """
    cursor.execute(sql, list(data.values()))
    conn.commit()
    cursor.close()

def main():
    tickers = get_sp500_tickers()
    conn = get_connection()

    success, failed = 0, []
    for i, symbol in enumerate(tickers, 1):
        try:
            data = fetch_fundamentals(symbol)
            upsert_company(conn, data)
            success += 1
            print(f"[{i}/{len(tickers)}] Inserted {symbol}")
        except Exception as e:
            failed.append(symbol)
            print(f"[{i}/{len(tickers)}] FAILED {symbol}: {e}")
        time.sleep(0.3)

    conn.close()
    print(f"\nDone. Success: {success}, Failed: {len(failed)}")
    if failed:
        print("Failed tickers:", failed)

if __name__ == "__main__":
    main()