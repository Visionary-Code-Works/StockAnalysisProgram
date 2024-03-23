"""stock_data_fetcher.py

This module provides the StockDataFetcher class, designed for fetching various
types of stock data, including historical data, moving averages, average
trading volume, and key financial metrics. It utilizes the yfinance library to
retrieve data from Yahoo Finance, offering a streamlined approach for stock
market analysis and data visualization.

The class is tailored for traders, investors, and analysts looking to perform
detailed stock analysis with ease.
"""

import yfinance as yf


class StockDataFetcher:
    """
    Fetches and processes stock data for a given ticker.

    This class offers functionalities to retrieve historical data, calculate
    moving averages, determine average trading volume, and gather financial
    metrics of a specific stock.
    """

    def __init__(self, ticker):
        """
        Initializes the StockDataFetcher with a stock ticker.

        Args:
            ticker (str): The stock ticker symbol for which the data is to be
            fetched.
        """
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def fetch_historical_data(self, period="1y"):
        """
        Retrieves historical stock data for the specified period.

        Args:
            period (str, optional): The time period for which to fetch the data
            (e.g., '1y' for one year). Defaults to '1y'.

        Returns:
            pandas.DataFrame: A DataFrame containing historical stock data for
            the specified period.
        """
        return self.stock.history(period=period)

    def calculate_moving_averages(self, data, window_sizes=[20, 50, 200]):
        """
        Calculates and returns moving averages for given window sizes.

        Args:
            data (pandas.DataFrame): The historical stock data.
            window_sizes (list of int, optional): The window sizes for which to
            calculate moving averages. Defaults to [20, 50, 200].

        Returns:
            dict: A dictionary with keys as window sizes and values as the
            corresponding moving averages.
        """
        moving_averages = {}
        for window in window_sizes:
            ma = data["Close"].rolling(window=window).mean()
            moving_averages[f"{window}-day MA"] = ma
        return moving_averages

    def get_average_volume(self, data):
        """
        Calculates and returns the average trading volume.

        Args:
            data (pandas.DataFrame): The historical stock data.

        Returns:
            float: The average trading volume for the stock.
        """
        return data["Volume"].mean()

    def get_financial_metrics(self):
        """
        Fetches and returns key financial metrics for the stock.

        Returns:
            dict: A dictionary containing key financial metrics such as market
            cap, PE ratios, and price to book value.
        """
        metrics = ["marketCap", "trailingPE", "forwardPE", "priceToBook"]
        return {metric: self.stock.info.get(metric, "N/A") for metric in metrics}
