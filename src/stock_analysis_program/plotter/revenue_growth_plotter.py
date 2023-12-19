"""revenue_growth_plotter.py

This module contains the RevenueGrowthPlotter class, which is responsible for
plotting the year-over-year revenue growth of a list of stocks. It utilizes the
RevenueGrowthFetcher class to fetch the necessary data and then visualizes it
in a bar chart format. This visualization aids in quickly understanding and
comparing the revenue growth trends of different companies.
"""

import matplotlib.pyplot as plt
from revenue_growth_fetcher import RevenueGrowthFetcher


class RevenueGrowthPlotter:
    """A class to plot the year-over-year revenue growth of stocks.

    This class provides a visual representation of the revenue growth of
    various stocks, which can be useful for investors and analysts to assess a
    company's financial performance over time.

    Attributes:
        fetcher (RevenueGrowthFetcher): An instance of RevenueGrowthFetcher to
        fetch revenue growth data.
    """

    def __init__(self, tickers):
        """Initializes RevenueGrowthPlotter with a list of stock tickers.

        Args:
            tickers (list of str): Stock tickers for which to plot revenue
            growth.
        """
        self.fetcher = RevenueGrowthFetcher(tickers)

    def plot_revenue_growth(self):
        """
        Plots the year-over-year revenue growth for each ticker.

        Fetches the revenue growth data using the fetcher instance and plots it
        in a bar chart, where each bar represents the revenue growth of a
        specific stock.
        """
        revenue_growth = self.fetcher.fetch_revenue_growth()

        # Prepare data for plotting
        tickers = list(revenue_growth.keys())
        growth_values = list(revenue_growth.values())

        plt.figure(figsize=(10, 6))
        plt.bar(tickers, growth_values, color='green')
        plt.title('Year-over-Year Revenue Growth')
        plt.xlabel('Ticker')
        plt.ylabel('Growth (%)')
        plt.grid(True)
        plt.show()
