# tests/test_plotter/test_stock_exchange_performance_plotter.py

import pytest
from src.stock_analysis_program import StockExchangePerformancePlotter

def test_stock_exchange_performance_plotter():
    plotter = StockExchangePerformancePlotter(["^GSPC"])
    assert plotter is not None, "StockExchangePerformancePlotter should be initialized."
