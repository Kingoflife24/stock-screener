import yfinance as yf
import time

def fetch_ticker_data(symbol):
    stock = yf.Ticker(symbol)
    info = stock.info
    return {
        "symbol": symbol,
        "pe_ratio": info.get("trailingPE"),
        "market_cap": info.get("marketCap"),
        "revenue_growth": info.get("revenueGrowth"),
        "sector": info.get("sector"),
    }

def fetch_multiple(symbols):
    results = []
    for sym in symbols:
        try:
            data = fetch_ticker_data(sym)
            results.append(data)
            print(f"Fetched {sym}")
        except Exception as e:
            print(f"Failed {sym}: {e}")
        time.sleep(0.5)  # be polite to the API, avoid rate limits
    return results

if __name__ == "__main__":
    test_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA"]
    data = fetch_multiple(test_tickers)
    for row in data:
        print(row)