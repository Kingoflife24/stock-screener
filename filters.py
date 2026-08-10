def pe_below(companies, max_pe):
    """Filter companies with PE ratio below threshold. Requires 'pe_ratio' key."""
    return [c for c in companies if c.get("pe_ratio") is not None and c["pe_ratio"] < max_pe]

def sector_is(companies, sector):
    return [c for c in companies if c.get("Sector") == sector]

def market_cap_above(companies, min_cap):
    return [c for c in companies if c.get("Marketcap") is not None and c["Marketcap"] > min_cap]

def apply_filters(companies, filters):
    """
    Apply a list of filter functions in sequence (AND logic).
    Each filter in `filters` is a tuple: (function, args_tuple)
    """
    result = companies
    for func, args in filters:
        result = func(result, *args)
    return result
