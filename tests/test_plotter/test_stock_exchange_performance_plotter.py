from unittest.mock import patch

import pandas as pd

from stock_analysis_program import StockExchangePerformancePlotter

def test_stock_exchange_performance_plotter():
    data = pd.DataFrame({"Close": [100, 110, 121]})
    with patch(
        "stock_analysis_program.plotter.stock_exchange_performance_plotter.yf.download",
        return_value=data,
    ):
        plotter = StockExchangePerformancePlotter(["^GSPC"])
        fig, ax = plotter.plot_performance("2024-01-01", "2024-01-03", show=False)

    assert fig is not None
    assert len(ax.lines) == 1
