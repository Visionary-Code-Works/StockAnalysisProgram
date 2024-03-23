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
from src.stock_analysis_program.fetcher.financial_metrics_fetcher import FinancialMetricsFetcher

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

    def plot_metrics(self):
        """Plots histograms of financial metrics for the given tickers.

        Fetches financial metrics using the FinancialMetricsFetcher instance
        and plots histograms for each metric. Metrics include market cap, PE
        ratio, forward PE, price to book ratio, and profit margins.

        The histograms provide a visual comparison of these metrics across the
        specified stocks.
        """
        financial_data = self.fetcher.fetch_financial_metrics()

        for column in financial_data.columns[1:]:  # Skip the 'Ticker' column
            plt.figure(figsize=(10, 6))
            # Check if the data is numeric and not empty
            if pd.to_numeric(financial_data[column], errors='coerce').notnull().all():
                plt.hist(financial_data[column].dropna(), bins=15, alpha=0.7)
                plt.title(f'Histogram of {column} for Selected Stocks')
                plt.xlabel(column)
                plt.ylabel('Frequency')
                plt.grid(True)
                plt.show()
            else:
                print(f"Skipping histogram for {column} as it contains non-numeric data.")
