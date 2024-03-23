# tests/test_plotter/test_stock_price_plotter.py

import pytest
from src.stock_analysis_program import StockPricePlotter

def test_stock_price_plotter_initialization():
    plotter = StockPricePlotter(['AAPL'])
    assert plotter is not None, "StockPricePlotter should be initialized."
