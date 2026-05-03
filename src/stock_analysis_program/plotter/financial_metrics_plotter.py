"""financial_metrics_plotter.py

This module contains the FinancialMetricsPlotter class, which is designed for
visualizing financial metrics of stocks. It uses the FinancialMetricsFetcher
class to fetch financial data and then plots these metrics in a histogram
format, providing a visual comparison across different stocks.

This class is particularly useful for financial analysts and investors who want
to compare and analyze financial metrics like market capitalization, PE ratio,
etc., across multiple stocks.
"""

import matplotlib.pyplot as plt
import pandas as pd
from ..fetcher.financial_metrics_fetcher import FinancialMetricsFetcher

class FinancialMetricsPlotter:
    """A class for plotting financial metrics of stocks.

    This class plots histograms of various financial metrics for a given list
    of stocks. It is useful for visually analyzing and comparing the financial
    health and performance of different stocks.

    Attributes:
        fetcher (FinancialMetricsFetcher): An instance of Financial
        MetricsFetcher used to fetch financial data for the given tickers.
    """

    def __init__(self, tickers):
        """Initializes FinancialMetricsPlotter with a list of stock tickers.

        Args:
            tickers (list of str): A list of stock ticker symbols for which to
            plot financial metrics.
        """
        self.fetcher = FinancialMetricsFetcher(tickers)

    def plot_metrics(self, show=True):
        """Plots histograms of financial metrics for the given tickers.

        Fetches financial metrics using the FinancialMetricsFetcher instance
        and plots histograms for each metric. Metrics include market cap, PE
        ratio, forward PE, price to book ratio, and profit margins.

        The histograms provide a visual comparison of these metrics across the
        specified stocks.
        """
        financial_data = self.fetcher.fetch_financial_metrics()

        figures = []
        for column in financial_data.columns[1:]:  # Skip the 'Ticker' column
            numeric_values = pd.to_numeric(financial_data[column], errors="coerce").dropna()
            if numeric_values.empty:
                continue

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.hist(numeric_values, bins=15, alpha=0.7)
            ax.set_title(f"Histogram of {column} for Selected Stocks")
            ax.set_xlabel(column)
            ax.set_ylabel("Frequency")
            ax.grid(True)
            figures.append((fig, ax))
            if show:
                plt.show()

        return figures
