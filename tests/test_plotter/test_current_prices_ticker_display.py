from unittest.mock import Mock, patch

from stock_analysis_program import CurrentPricesTickerDisplay

def test_current_prices_ticker_display_initialization():
    display = CurrentPricesTickerDisplay(["aapl"], 10)
    assert display.tickers == ["AAPL"]


def test_current_prices_ticker_display_fetches_prices():
    stock = Mock()
    stock.info = {"currentPrice": 123.45}

    with patch("stock_analysis_program.plotter.current_prices_ticker_display.yf.Ticker", return_value=stock):
        display = CurrentPricesTickerDisplay(["AAPL"], 10)
        prices = display.fetch_current_prices()

    assert prices == {"AAPL": 123.45}
