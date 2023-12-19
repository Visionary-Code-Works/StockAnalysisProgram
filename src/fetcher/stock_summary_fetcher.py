""" stock_summary_fetcher.py

This module contains the StockSummaryFetcher class, which is designed to fetch
and provide summary information for a given list of stock tickers using the
yfinance library. The summaries include key details such as company name,
sector, industry, financial metrics, and more.

The class is useful for getting a quick overview of various stocks in an easy
and streamlined manner, making it a valuable tool for financial analysis and
stock market research.
"""

import yfinance as yf

class StockSummaryFetcher:
    """
    A class that fetches summary information for a list of stock tickers.

    This class utilizes the yfinance library to fetch and compile a summary for
    each stock ticker provided. The summary includes essential information such
    as the company's name, sector, industry, stock exchange, and key financial
    metrics.
    """

    def __init__(self, tickers):
        """
        Initializes the StockSummaryFetcher with a list of stock tickers.

        This constructor accepts a single ticker or a list of tickers and
        stores them for further processing.

        Args:
            tickers (str or list of str): The stock ticker(s) for which the
            summary information is to be fetched. Can be a single ticker (str)
            or a list of tickers.
        """
        self.tickers = tickers if isinstance(tickers, list) else [tickers]

    def fetch_summary(self, ticker):
        """
        Fetches and returns the summary information for a given stock ticker.

        This method retrieves various details about a stock, such as name,
        sector, industry, and financial metrics using the yfinance library.

        Args:
            ticker (str): The stock ticker for which the summary is to be
            fetched.

        Returns:
            dict: A dictionary containing the summary information of the stock.
            Includes name, sector, industry, country, exchange, website,
            business summary, and key financial data.
        """
        stock = yf.Ticker(ticker)
        info = stock.info
        return {
            'Name': info.get('longName'),
            'Sector': info.get('sector'),
            'Industry': info.get('industry'),
            'Country': info.get('country'),
            'Exchange': info.get('exchange'),
            'Website': info.get('website'),
            'Summary': info.get('longBusinessSummary'),
            'Currency': info.get('currency'),
            'Quote Type': info.get('quoteType'),
            'Market': info.get('market'),
            'Ticker': ticker,
            'Previous Close': info.get('previousClose'),
            'Day Range': info.get('regularMarketDayRange'),
            '52 Week Range': info.get('fiftyTwoWeekRange'),
            'Market Cap': info.get('marketCap'),
            'Average Volume': info.get('averageVolume'),
            'P/E Ratio': info.get('trailingPE')
        }

    def get_summaries(self):
        """
        Retrieves the stock summaries for all tickers specified during
        initialization.

        Iterates over the list of tickers and uses the fetch_summary method to
        get the summary for each ticker.

        Returns:
            list of dict: A list of dictionaries, each containing the summary
            information of a stock ticker.
        """
        return [self.fetch_summary(ticker) for ticker in self.tickers]
