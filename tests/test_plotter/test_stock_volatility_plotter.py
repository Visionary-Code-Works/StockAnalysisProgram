# tests/test_plotter/test_stock_volatility_plotter.py

import pytest
from src.plotter.stock_volatility_plotter import StockVolatilityPlotter

def test_stock_volatility_plotter_initialization():
    plotter = StockVolatilityPlotter(["AAPL"])
    assert plotter is not None, "StockVolatilityPlotter should be initialized."
