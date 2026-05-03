from unittest.mock import Mock, patch

import pandas as pd

from stock_analysis_program import StockDataFetcher

def test_stock_data_fetcher():
    with patch("stock_analysis_program.fetcher.stock_data_fetcher.yf.Ticker") as ticker:
        ticker.return_value = Mock()
        fetcher = StockDataFetcher("aapl")

    assert fetcher.ticker == "AAPL"
    ticker.assert_called_once_with("AAPL")


def test_stock_data_fetcher_calculates_moving_averages():
    fetcher = StockDataFetcher.__new__(StockDataFetcher)
    fetcher.ticker = "AAPL"
    data = pd.DataFrame({"Close": [1, 2, 3], "Volume": [10, 20, 30]})

    moving_averages = fetcher.calculate_moving_averages(data, window_sizes=[2])

    assert "2-day MA" in moving_averages
    assert moving_averages["2-day MA"].iloc[-1] == 2.5
    assert fetcher.get_average_volume(data) == 20
