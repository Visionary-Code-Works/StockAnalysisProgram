from unittest.mock import Mock, patch

from stock_analysis_program.fetcher import FinancialMetricsFetcher

def test_financial_metrics_fetcher():
    stock = Mock()
    stock.info = {
        "marketCap": 100,
        "trailingPE": 20,
        "forwardPE": 18,
        "priceToBook": 3,
        "profitMargins": 0.25,
    }

    with patch("stock_analysis_program.fetcher.financial_metrics_fetcher.yf.Ticker", return_value=stock):
        fetcher = FinancialMetricsFetcher(["aapl"])
        metrics = fetcher.fetch_financial_metrics()

    assert "AAPL" in metrics["Ticker"].values
    assert metrics.loc[0, "Market Cap"] == 100
