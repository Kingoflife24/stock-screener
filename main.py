import argparse
from db import get_all_companies
from filters import sector_is, market_cap_above, pe_below, revenue_growth_above, apply_filters

def parse_args():
    parser = argparse.ArgumentParser(description="S&P 500 Stock Screener")
    parser.add_argument("--sector", type=str, help="Filter by sector (e.g. Technology)")
    parser.add_argument("--min-cap", type=float, help="Minimum market cap (e.g. 500000000000)")
    parser.add_argument("--max-pe", type=float, help="Maximum PE ratio (e.g. 25)")
    parser.add_argument("--min-growth", type=float, help="Minimum revenue growth as decimal (e.g. 0.1 for 10%%)")
    return parser.parse_args()

def main():
    args = parse_args()
    companies = get_all_companies()

    filters = []
    if args.sector:
        filters.append((sector_is, (args.sector,)))
    if args.min_cap:
        filters.append((market_cap_above, (args.min_cap,)))
    if args.max_pe:
        filters.append((pe_below, (args.max_pe,)))
    if args.min_growth:
        filters.append((revenue_growth_above, (args.min_growth,)))

    results = apply_filters(companies, filters)

    print(f"Results: {len(results)} companies")
    for c in results:
        pe = c.get("Pe_ratio")
        pe_str = f"{pe:.1f}" if pe else "N/A"
        mc = c.get("Marketcap")
        mc_str = f"{mc:>18,}" if mc is not None else f"{'N/A':>18}"
        print(f"{c['Symbol']:<8} {c['Sector']:<25} MarketCap: {mc_str}  PE: {pe_str}")
if __name__ == "__main__":
    main()