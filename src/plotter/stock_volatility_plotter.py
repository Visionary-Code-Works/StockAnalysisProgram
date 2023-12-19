"""stock_volatility_plotter.py

This module contains the StockVolatilityPlotter class, which focuses on
calculating and visualizing the rolling volatility of stock prices. It fetches
historical price data and calculates volatility based on the daily price
changes. This class is beneficial for investors and analysts to assess the risk
profile and stability of stocks.
"""

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


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
        self.tickers = tickers if isinstance(tickers, list) else [tickers]

    def plot_volatility(self, start_date, end_date, window_size=30):
        """
        Calculates and plots the rolling volatility for each ticker.

        Args:
            start_date (str): Start date for the data in 'YYYY-MM-DD' format.
            end_date (str): End date for the data in 'YYYY-MM-DD' format.
            window_size (int, optional): Window size in days for calculating
            rolling volatility. Defaults to 30.
        """
        plt.figure(figsize=(12, 8))

        for ticker in self.tickers:
            data = yf.download(ticker, start=start_date, end=end_date)
            # Calculate daily returns
            daily_returns = data['Close'].pct_change()
            # Calculate rolling standard deviation (volatility)
            rolling_volatility = daily_returns.rolling(window=window_size).std() * (252 ** 0.5)  # Annualized

            plt.plot(rolling_volatility, label=f'{ticker} Volatility')

        plt.title(f'{window_size}-Day Rolling Volatility (Annualized)')
        plt.xlabel('Date')
        plt.ylabel('Volatility')
        plt.legend()
        plt.grid(True)
        plt.show()
