from unittest.mock import patch

import pandas as pd

from stock_analysis_program import StockVolatilityPlotter

def test_stock_volatility_plotter_initialization():
    data = pd.DataFrame({"Close": [100, 101, 103, 102]})
    with patch(
        "stock_analysis_program.plotter.stock_volatility_plotter.yf.download",
        return_value=data,
    ):
        plotter = StockVolatilityPlotter(["AAPL"])
        fig, ax = plotter.plot_volatility("2024-01-01", "2024-01-04", show=False)

    assert fig is not None
    assert len(ax.lines) == 1
