# tests/test_plotter/test_current_prices_ticker_display.py

import pytest
from src.stock_analysis_program import CurrentPricesTickerDisplay

def test_current_prices_ticker_display_initialization():
    display = CurrentPricesTickerDisplay(["AAPL"], 10)
    assert display is not None, "CurrentPricesTickerDisplay should be initialized."
