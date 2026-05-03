from unittest.mock import Mock, patch

import pandas as pd
import pytest

from stock_analysis_program import RevenueGrowthFetcher

def test_revenue_growth_fetcher_returns_latest_growth():
    stock = Mock()
    stock.financials = pd.DataFrame(
        [[120, 100]],
        index=["Total Revenue"],
        columns=["2024", "2023"],
    )

    with patch("stock_analysis_program.fetcher.revenue_growth_fetcher.yf.Ticker", return_value=stock):
        fetcher = RevenueGrowthFetcher(["aapl"])
        growth = fetcher.fetch_revenue_growth()

    assert growth["AAPL"] == pytest.approx(0.2)
