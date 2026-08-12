import pandas as pd
import requests
from io import StringIO

def get_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    tables = pd.read_html(StringIO(response.text))
    sp500_table = tables[0]
    tickers = sp500_table["Symbol"].tolist()
    tickers = [t.replace(".", "-") for t in tickers]
    return tickers

if __name__ == "__main__":
    tickers = get_sp500_tickers()
    print(f"Total tickers: {len(tickers)}")
    print(tickers[:10])