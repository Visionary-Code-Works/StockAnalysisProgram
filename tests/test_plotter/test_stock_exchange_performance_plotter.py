# tests/test_plotter/test_stock_exchange_performance_plotter.py

import pytest
from src.plotter.stock_exchange_performance_plotter import StockExchangePerformancePlotter

def test_stock_exchange_performance_plotter_initialization():
    plotter = StockExchangePerformancePlotter(["^GSPC"])
    assert plotter is not None, "StockExchangePerformancePlotter should be initialized."
