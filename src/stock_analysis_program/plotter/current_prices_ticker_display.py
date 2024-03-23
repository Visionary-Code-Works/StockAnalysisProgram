"""current_prices_ticker_display.py

Provides a class to display current stock prices in a ticker-like format. This
module is designed for real-time monitoring of stock prices, fetching the
latest prices at regular intervals. It is particularly useful for traders and
investors who need to keep an eye on the market movements of selected stocks.

The class facilitates a dynamic display of stock prices, simulating a stock
ticker tape seen in trading platforms or financial news channels.
"""

import os
import time
import yfinance as yf

class CurrentPricesTickerDisplay:
    """
    A class for displaying current prices of a list of stock tickers in a
    ticker-like format.

    This class fetches the current prices of given stock tickers and displays
    them in a continuously updating format, emulating a stock ticker tape. The
    display interval can be customized.
    """

    def __init__(self, tickers, interval=10):
        """
        Initializes the CurrentPricesTickerDisplay with a list of stock tickers
        and a display interval.

        Args:
            tickers (list of str): List of stock ticker symbols whose current
            prices are to be displayed.
            interval (int, optional): Time interval in seconds between updates
            of the ticker display. Defaults to 10 seconds.
        """
        self.tickers = tickers if isinstance(tickers, list) else [tickers]
        self.interval = interval

    def fetch_current_prices(self):
        """
        Fetches the current trading prices for each stock ticker.

        Retrieves the latest trading price for each stock ticker in the list
        from Yahoo Finance using the yfinance library.

        Returns:
            dict: A dictionary with stock tickers as keys and their
            corresponding current prices as values.
        """
        prices = {}
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            price = stock.info.get('currentPrice', 'N/A')
            prices[ticker] = price
        return prices

    def display_ticker(self):
        """
        Displays the current prices of stock tickers in a rolling ticker format.

        Continuously updates and displays the current prices for each ticker,
        refreshing at the specified interval. The display can be stopped with a
        keyboard interrupt.
        """
        try:
            while True:
                prices = self.fetch_current_prices()
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                for ticker, price in prices.items():
                    print(f"{ticker}: {price}", end=" | ")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("\nStopped the rolling ticker.")
