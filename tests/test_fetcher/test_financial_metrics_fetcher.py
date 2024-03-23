# tests/test_fetcher/test_financial_metrics_fetcher.py

import pytest
from src.stock_analysis_program.fetcher import FinancialMetricsFetcher

def test_financial_metrics_fetcher():
    fetcher = FinancialMetricsFetcher(['AAPL'])
    metrics = fetcher.fetch_financial_metrics()
    assert 'AAPL' in metrics, "AAPL should be in the fetched financial metrics."
