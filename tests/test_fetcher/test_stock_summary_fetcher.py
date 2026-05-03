from unittest.mock import Mock, patch

from stock_analysis_program import StockSummaryFetcher

def test_stock_summary_fetcher_returns_summary():
    stock = Mock()
    stock.info = {"longName": "Apple Inc.", "sector": "Technology"}

    with patch("stock_analysis_program.fetcher.stock_summary_fetcher.yf.Ticker", return_value=stock):
        fetcher = StockSummaryFetcher(["aapl"])
        summaries = fetcher.get_summaries()

    assert summaries[0]["Ticker"] == "AAPL"
    assert summaries[0]["Name"] == "Apple Inc."
