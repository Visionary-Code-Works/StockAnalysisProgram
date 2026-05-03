"""stock_exchange_performance_plotter.py

This module provides the StockExchangePerformancePlotter class, which is
designed to compare and visualize the performance of different stock indices.

It plots the normalized closing prices of the indices, allowing for an easy
comparison of their relative performance over a selected time frame. This class
is particularly useful for financial analysts and investors interested in
comparing market trends and index performances.
"""

import yfinance as yf
import matplotlib.pyplot as plt

from .._utils import normalize_tickers, require_columns

class StockExchangePerformancePlotter:
    """A class for comparing the performance of different stock indices.

    Plots the normalized closing prices of various stock indices to compare
    their performance over time. Useful for visualizing market trends and
    understanding relative index movements.

    Attributes:
        indices (list of str): A list of stock index symbols to compare.
    """

    def __init__(self, indices):
        """
        Initializes the StockExchangePerformancePlotter with a list of stock
        indices.

        Args:
            indices (list of str): Stock index symbols for comparison.
        """
        self.indices = normalize_tickers(indices)

    def plot_performance(self, start_date, end_date, show=True):
        """Plots the normalized closing prices of the indices for comparison.

        Args:
            start_date (str): The start date for fetching data in 'YYYY-MM-DD'
            format.
            end_date (str): The end date for fetching data in 'YYYY-MM-DD'
            format.

        Fetches data for each index and plots their normalized closing prices
        to visualize and compare their performance over the specified time
        period.
        """
        fig, ax = plt.subplots(figsize=(14, 8))
        for index in self.indices:
            data = yf.download(index, start=start_date, end=end_date)
            require_columns(data, ["Close"], index)
            normalized_data = data['Close'] / data['Close'].iloc[0]
            ax.plot(normalized_data, label=index)

        ax.set_title('Comparative Performance of Stock Indices')
        ax.set_xlabel('Date')
        ax.set_ylabel('Normalized Closing Price')
        ax.legend()
        ax.grid(True)
        if show:
            plt.show()
        return fig, ax
