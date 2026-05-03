from unittest.mock import patch

from stock_analysis_program import RevenueGrowthPlotter

def test_revenue_growth_plotter_returns_figure():
    with patch(
        "stock_analysis_program.plotter.revenue_growth_plotter.RevenueGrowthFetcher"
    ) as fetcher:
        fetcher.return_value.fetch_revenue_growth.return_value = {"AAPL": 0.2}
        plotter = RevenueGrowthPlotter(["AAPL"])
        fig, ax = plotter.plot_revenue_growth(show=False)

    assert fig is not None
    assert len(ax.patches) == 1
