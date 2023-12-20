# tests/test_fetcher/test_stock_data_fetcher.py

import pytest
from src.fetcher.stock_data_fetcher import StockDataFetcher

def test_stock_data_fetcher():
    fetcher = StockDataFetcher("AAPL")
    assert fetcher is not None, "StockDataFetcher should be initialized."
