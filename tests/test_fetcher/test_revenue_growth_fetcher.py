# tests/test_fetcher/test_revenue_growth_fetcher.py

import pytest
from src.stock_analysis_program import RevenueGrowthFetcher

def test_revenue_growth_fetcher_initialization():
    fetcher = RevenueGrowthFetcher(["AAPL"])
    assert fetcher is not None, "RevenueGrowthFetcher should be initialized."
