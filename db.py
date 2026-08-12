import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),   
        database="sp500_companies"
    )

def get_all_companies():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT Symbol, Shortname, Sector, Marketcap, Revenuegrowth, Pe_ratio FROM companies")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

if __name__ == "__main__":
    from filters import sector_is, market_cap_above, apply_filters

    companies = get_all_companies()
    print(f"Total companies: {len(companies)}")

    # Tech AND market cap > $500B
    filtered = apply_filters(companies, [
        (sector_is, ("Technology",)),
        (market_cap_above, (500_000_000_000,)),
    ])

    print(f"Tech + Large cap: {len(filtered)}")
    for c in filtered:
        print(c["Symbol"], c["Sector"], c["Marketcap"])