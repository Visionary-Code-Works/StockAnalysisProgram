"""stock_price_plotter.py

This module contains the StockPricePlotter class, which is designed for
visualizing stock prices and their moving averages. It uses yfinance to fetch
historical data and matplotlib for plotting. The class is particularly useful
for traders and investors who wish to analyze stock price trends and patterns
over time.
"""

import yfinance as yf
import matplotlib.pyplot as plt

class StockPricePlotter:
    """
    A class for plotting stock prices and moving averages.

    This class provides functionalities to plot closing prices and moving
    averages for a list of stocks. It can be used for technical analysis and to
    visually assess stock performance over a selected time period.
    """

    def __init__(self, tickers):
        """
        Initializes the StockPricePlotter with a list of stock tickers.

        Args:
            tickers (list of str): Stock tickers to plot prices and moving
            averages for.
        """
        self.tickers = tickers if isinstance(tickers, list) else [tickers]

    def plot_closing_prices(self, start_date, end_date):
        """
        Plots the closing prices of the stocks over a specified period.

        Args:
            start_date (str): Start date for the data in 'YYYY-MM-DD' format.
            end_date (str): End date for the data in 'YYYY-MM-DD' format.
        """
        for ticker in self.tickers:
            data = yf.download(ticker, start=start_date, end=end_date)
            plt.figure(figsize=(10, 6))
            plt.plot(data['Close'], label=f'{ticker} Close Price')
            plt.title(f'{ticker} Closing Prices')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid(True)
            plt.show()

    def plot_moving_averages(self, start_date, end_date, window_sizes=[20, 50]):
        """
        Plots moving averages along with closing prices for the stocks.

        Args:
            start_date (str): Start date for the data in 'YYYY-MM-DD' format.
            end_date (str): End date for the data in 'YYYY-MM-DD' format.
            window_sizes (list of int, optional): Window sizes for calculating
            moving averages. Defaults to [20, 50].
        """
        for ticker in self.tickers:
            data = yf.download(ticker, start=start_date, end=end_date)
            plt.figure(figsize=(10, 6))
            plt.plot(data['Close'], label=f'{ticker} Closing Prices', alpha=0.5)
            for window in window_sizes:
                ma = data['Close'].rolling(window=window).mean()
                plt.plot(ma, label=f'{window}-Day MA')
            plt.title(f'{ticker} Closing Prices and Moving Averages')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.grid(True)
            plt.show()
