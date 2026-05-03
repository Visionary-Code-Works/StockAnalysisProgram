from unittest.mock import patch

import pandas as pd

from stock_analysis_program import StockPricePlotter

def test_stock_price_plotter_initialization():
    plotter = StockPricePlotter(["aapl"])
    assert plotter.tickers == ["AAPL"]


def test_stock_price_plotter_returns_figures():
    data = pd.DataFrame({"Close": [1, 2, 3]})
    with patch("stock_analysis_program.plotter.stock_price_plotter.yf.download", return_value=data):
        plotter = StockPricePlotter(["AAPL"])
        figures = plotter.plot_closing_prices("2024-01-01", "2024-01-03", show=False)

    assert len(figures) == 1
    assert figures[0][0] is not None
