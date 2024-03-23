# tests/test_fetcher/test_stock_data_fetcher.py

import pytest
from src.stock_analysis_program import StockDataFetcher

def test_stock_data_fetcher():
    fetcher = StockDataFetcher("AAPL")
    assert fetcher is not None, "StockDataFetcher should be initialized."
