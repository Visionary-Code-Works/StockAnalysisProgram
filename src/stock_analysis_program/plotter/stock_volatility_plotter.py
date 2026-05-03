"""stock_volatility_plotter.py

This module contains the StockVolatilityPlotter class, which focuses on
calculating and visualizing the rolling volatility of stock prices. It fetches
historical price data and calculates volatility based on the daily price
changes. This class is beneficial for investors and analysts to assess the risk
profile and stability of stocks.
"""

import yfinance as yf
import matplotlib.pyplot as plt

from .._utils import normalize_tickers, require_columns


class StockVolatilityPlotter:
    """
    A class to calculate and plot the rolling volatility of stocks.

    This class uses historical price data to calculate and visualize the
    rolling volatility of stocks, offering insights into their price stability
    and risk profile.
    """

    def __init__(self, tickers):
        """Initializes the StockVolatilityPlotter with a list of stock tickers.

        Args:
            tickers (list of str): Stock tickers to analyze for volatility.
        """
        self.tickers = normalize_tickers(tickers)

    def plot_volatility(self, start_date, end_date, window_size=30, show=True):
        """
        Calculates and plots the rolling volatility for each ticker.

        Args:
            start_date (str): Start date for the data in 'YYYY-MM-DD' format.
            end_date (str): End date for the data in 'YYYY-MM-DD' format.
            window_size (int, optional): Window size in days for calculating
            rolling volatility. Defaults to 30.
        """
        fig, ax = plt.subplots(figsize=(12, 8))

        for ticker in self.tickers:
            data = yf.download(ticker, start=start_date, end=end_date)
            require_columns(data, ["Close"], ticker)
            # Calculate daily returns
            daily_returns = data['Close'].pct_change()
            # Calculate rolling standard deviation (volatility)
            rolling_volatility = daily_returns.rolling(window=window_size).std() * (252 ** 0.5)  # Annualized

            ax.plot(rolling_volatility, label=f'{ticker} Volatility')

        ax.set_title(f'{window_size}-Day Rolling Volatility (Annualized)')
        ax.set_xlabel('Date')
        ax.set_ylabel('Volatility')
        ax.legend()
        ax.grid(True)
        if show:
            plt.show()
        return fig, ax
