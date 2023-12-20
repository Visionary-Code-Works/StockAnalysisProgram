"""financial_metrics_fetcher.py

This module contains the FinancialMetricsFetcher class. It is designed to fetch
financial metrics such as market capitalization, P/E ratio, forward P/E, price
to book ratio, and profit margins for a given list of stock tickers. This class
utilizes the yfinance library to retrieve financial data from Yahoo Finance,
making it useful for financial analysis and comparisons across different stocks.

The class is ideal for investors and financial analysts who need to quickly
compare fundamental financial metrics of various companies.
"""

import yfinance as yf
import pandas as pd

class FinancialMetricsFetcher:
    """
    A class that fetches financial metrics for a list of stock tickers.

    This class provides functionality to retrieve important financial metrics
    for stocks. It is useful for conducting financial analysis and comparison
    across different stocks in a portfolio or watchlist.
    """

    def __init__(self, tickers):
        """
        Initializes the FinancialMetricsFetcher with a list of stock tickers.

        This constructor stores the list of tickers for which financial metrics
        will be fetched.

        Args:
            tickers (list of str): A list of stock ticker symbols (e.g.,
            ['AAPL', 'MSFT']) for which financial metrics are to be fetched.
        """
        self.tickers = tickers if isinstance(tickers, list) else [tickers]

    def fetch_financial_metrics(self):
        """
        Fetches and compiles financial metrics for each ticker in the list.

        This method retrieves key financial metrics for each stock ticker and
        returns them in a Pandas DataFrame. Metrics include market cap, P/E
        ratio, forward P/E, price to book ratio, and profit margins.

        Returns:
            pandas.DataFrame: A DataFrame containing the financial metrics for
            each ticker. Each row corresponds to a stock ticker, with columns
            for each financial metric.
        """
        financial_data_list = []

        financial_data = pd.DataFrame()
        for ticker in self.tickers:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Extract desired metrics and add them to the DataFrame
            financial_data_list.append({
                'Ticker': ticker,
                'Market Cap': info.get('marketCap'),
                'PE Ratio': info.get('trailingPE'),
                'Forward PE': info.get('forwardPE'),
                'Price to Book': info.get('priceToBook'),
                'Profit Margins': info.get('profitMargins')
            })

        financial_data = pd.DataFrame(financial_data_list)
        return financial_data
