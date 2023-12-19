"""revenue_growth_fetcher.py

This module contains the RevenueGrowthFetcher class, which is designed to fetch
and calculate the year-over-year revenue growth for a given list of stock
tickers. It leverages the yfinance library to access historical financial data,
making it a valuable tool for financial analysis, especially in assessing
company performance over time.

The class provides a simple way to measure and compare the revenue growth of
different companies, aiding in investment decisions and market analysis.
"""

import yfinance as yf

class RevenueGrowthFetcher:
    """
    Fetches year-over-year revenue growth for a list of stock tickers.

    This class accesses historical income statement data to calculate the
    year-over-year revenue growth percentage for each provided stock ticker.
    """

    def __init__(self, tickers):
        """
        Initializes the RevenueGrowthFetcher with a list of stock tickers.

        Args:
            tickers (list of str): Stock tickers to fetch the revenue growth
            for.
        """
        self.tickers = tickers if isinstance(tickers, list) else [tickers]

    def fetch_revenue_growth(self):
        """
        Calculates the most recent year-over-year revenue growth for each
        ticker.

        Returns:
            dict: A dictionary with tickers as keys and their respective
            year-over-year revenue growth percentages as values.
        """
        growth_data = {}
        for ticker in self.tickers:
            company = yf.Ticker(ticker)
            income_statement = company.financials
            if 'Total Revenue' in income_statement.index:
                revenue = income_statement.loc['Total Revenue']
                revenue_growth = revenue.pct_change(periods=-1)  # Negative periods for year-over-year growth
                growth_data[ticker] = revenue_growth.dropna().iloc[0]  # Most recent growth value
            else:
                growth_data[ticker] = None
        return growth_data
