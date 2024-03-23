# tests/test_fetcher/test_stock_summary_fetcher.py

import pytest
from src.stock_analysis_program import StockSummaryFetcher

def test_stock_summary_fetcher_initialization():
    fetcher = StockSummaryFetcher(["AAPL"])
    assert fetcher is not None, "StockSummaryFetcher should be initialized."
