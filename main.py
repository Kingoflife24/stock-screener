import argparse
from db import get_all_companies
from filters import sector_is, market_cap_above, apply_filters

def parse_args():
    parser = argparse.ArgumentParser(description="S&P 500 Stock Screener")
    parser.add_argument("--sector", type=str, help="Filter by sector (e.g. Technology)")
    parser.add_argument("--min-cap", type=float, help="Minimum market cap (e.g. 500000000000)")
    return parser.parse_args()

def main():
    args = parse_args()
    companies = get_all_companies()

    filters = []
    if args.sector:
        filters.append((sector_is, (args.sector,)))
    if args.min_cap:
        filters.append((market_cap_above, (args.min_cap,)))

    results = apply_filters(companies, filters)

    print(f"Results: {len(results)} companies")
    for c in results:
        print(f"{c['Symbol']:<8} {c['Sector']:<25} MarketCap: {c['Marketcap']:,}")

if __name__ == "__main__":
    main()