from filters import sector_is, market_cap_above, pe_below, revenue_growth_above, apply_filters

sample_companies = [
    {"Symbol": "AAPL", "Sector": "Technology", "Marketcap": 3_000_000_000_000, "Pe_ratio": 35.0, "Revenuegrowth": 0.16},
    {"Symbol": "XOM", "Sector": "Energy", "Marketcap": 450_000_000_000, "Pe_ratio": 14.0, "Revenuegrowth": 0.02},
    {"Symbol": "JNJ", "Sector": "Healthcare", "Marketcap": 380_000_000_000, "Pe_ratio": None, "Revenuegrowth": 0.05},
]

def test_sector_is():
    result = sector_is(sample_companies, "Technology")
    assert len(result) == 1
    assert result[0]["Symbol"] == "AAPL"

def test_market_cap_above():
    result = market_cap_above(sample_companies, 400_000_000_000)
    symbols = [c["Symbol"] for c in result]
    assert "AAPL" in symbols
    assert "XOM" in symbols
    assert "JNJ" not in symbols

def test_pe_below():
    result = pe_below(sample_companies, 20)
    symbols = [c["Symbol"] for c in result]
    assert symbols == ["XOM"]

def test_pe_below_handles_none():
    result = pe_below(sample_companies, 100)
    symbols = [c["Symbol"] for c in result]
    assert "JNJ" not in symbols

def test_revenue_growth_above():
    result = revenue_growth_above(sample_companies, 0.1)
    symbols = [c["Symbol"] for c in result]
    assert symbols == ["AAPL"]

def test_apply_filters_chains_with_and_logic():
    result = apply_filters(sample_companies, [
        (sector_is, ("Technology",)),
        (market_cap_above, (1_000_000_000_000,)),
    ])
    symbols = [c["Symbol"] for c in result]
    assert symbols == ["AAPL"]

def test_apply_filters_no_filters_returns_all():
    result = apply_filters(sample_companies, [])
    assert len(result) == 3