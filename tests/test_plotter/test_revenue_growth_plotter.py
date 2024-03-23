# tests/test_plotter/test_revenue_growth_plotter.py

import pytest
from src.stock_analysis_program import RevenueGrowthPlotter

def test_revenue_growth_plotter_initialization():
    plotter = RevenueGrowthPlotter(["AAPL"])
    assert plotter is not None, "RevenueGrowthPlotter should be initialized."
