""" main.py

This script provides a user interface to interact with various stock analysis
functionalities. It includes options to fetch and plot stock data, summarize
financial metrics, and visualize stock performance.

The script uses a menu-driven approach to allow users to choose from different
stock analysis options, including data fetching, summary retrieval, and various
plotting capabilities for stocks and financial indices.
"""

from .__init__ import (
    StockDataFetcher,
    StockSummaryFetcher,
    FinancialMetricsFetcher,
    RevenueGrowthFetcher,
    StockPricePlotter,
    FinancialMetricsPlotter,
    RevenueGrowthPlotter,
    StockVolatilityPlotter,
    StockExchangePerformancePlotter,
    CurrentPricesTickerDisplay,
)


def use_stock_data_fetcher():
    """
    Interacts with StockDataFetcher to fetch historical data, moving averages,
    average volume, and financial metrics for a specific stock ticker.

    Users are prompted to enter a stock ticker. The function then displays
    historical data, moving averages, average trading volume, and key financial
    metrics for the entered ticker.
    """
    ticker = input("Enter a stock ticker (e.g., AAPL, GOOGL): ")
    fetcher = StockDataFetcher(ticker)
    historical_data = fetcher.fetch_historical_data()
    moving_averages = fetcher.calculate_moving_averages(historical_data)
    average_volume = fetcher.get_average_volume(historical_data)
    financial_metrics = fetcher.get_financial_metrics()

    print(f"Moving Averages for {ticker}: {moving_averages}")
    print(f"Average Volume for {ticker}: {average_volume}")
    print(f"Financial Metrics for {ticker}: {financial_metrics}")


def use_stock_summary_fetcher():
    """
    Utilizes StockSummaryFetcher to retrieve and display summary information
    for a list of stock tickers.

    Users can enter multiple stock tickers separated by commas. The function
    fetches and displays a summary for each ticker, including name, sector,
    industry, and other key details.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas (e.g., GOOGL, AAPL): "
    ).split(",")
    fetcher = StockSummaryFetcher([ticker.strip() for ticker in tickers])
    summaries = fetcher.get_summaries()

    for summary in summaries:
        print(f"\nSummary for {summary['Ticker']}:\n")
        for key, value in summary.items():
            print(f"{key}: {value if value is not None else 'N/A'}")


def use_financial_metrics_fetcher():
    """
    Uses FinancialMetricsFetcher to fetch and display financial metrics for a
    list of stock tickers.

    This function allows users to enter multiple tickers and displays financial
    metrics such as market cap, PE ratio, forward PE, and profit margins for
    each ticker.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for financial metrics (e.g., AAPL, MSFT): "
    ).split(",")
    fetcher = FinancialMetricsFetcher([ticker.strip() for ticker in tickers])
    financial_metrics = fetcher.fetch_financial_metrics()

    print("\nFinancial Metrics:")
    print(financial_metrics)


def use_revenue_growth_fetcher():
    """
    Interacts with RevenueGrowthFetcher to fetch and display year-over-year
    revenue growth for a list of stock tickers.

    After users input stock tickers, the function calculates and displays the
    year-over-year revenue growth percentage for each ticker.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for revenue growth (e.g., AAPL, MSFT): "
    ).split(",")
    fetcher = RevenueGrowthFetcher([ticker.strip() for ticker in tickers])
    revenue_growth = fetcher.fetch_revenue_growth()

    print("\nYear-over-Year Revenue Growth:")
    for ticker, growth in revenue_growth.items():
        print(
            f"{ticker}: {growth:.2%}"
            if growth is not None
            else f"{ticker}: Data not available"
        )


def use_stock_price_plotter():
    """
    Uses StockPricePlotter to plot closing prices and moving averages for a
    list of stock tickers.

    Users input stock tickers and a date range. The function then plots the
    closing prices and moving averages for the selected period for each ticker.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for price plotting (e.g., AAPL, MSFT): "
    ).split(",")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    plotter = StockPricePlotter([ticker.strip() for ticker in tickers])
    plotter.plot_closing_prices(start_date, end_date)
    plotter.plot_moving_averages(start_date, end_date)


def use_financial_metrics_plotter():
    """
    Utilizes FinancialMetricsPlotter to create histograms of financial metrics
    for a list of stock tickers.

    After receiving a list of tickers from the user, this function plots
    histograms for key financial metrics like market cap and PE ratio for each
    ticker.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for financial metrics plotting (e.g., AAPL, MSFT): "
    ).split(",")
    plotter = FinancialMetricsPlotter([ticker.strip() for ticker in tickers])
    plotter.plot_metrics()


def use_revenue_growth_plotter():
    """
    Leverages RevenueGrowthPlotter to plot the revenue growth of a list of
    stock tickers.

    Users provide stock tickers, and the function visualizes the year-over-year
    revenue growth for each ticker in a bar chart format.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for revenue growth plotting (e.g., AAPL, MSFT): "
    ).split(",")
    plotter = RevenueGrowthPlotter([ticker.strip() for ticker in tickers])
    plotter.plot_revenue_growth()


def use_stock_volatility_plotter():
    """
    Interacts with StockVolatilityPlotter to plot the rolling volatility of a
    list of stock tickers.

    Users enter stock tickers and a date range, and the function plots the
    calculated rolling volatility for each ticker over the specified period.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for volatility plotting (e.g., AAPL, MSFT): "
    ).split(",")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    plotter = StockVolatilityPlotter([ticker.strip() for ticker in tickers])
    plotter.plot_volatility(start_date, end_date)


def use_stock_exchange_performance_plotter():
    """
    Uses StockExchangePerformancePlotter to compare and visualize the
    performance of different stock indices.

    Users input symbols of stock indices and a date range, and the function
    plots the normalized closing prices of these indices for comparative
    analysis.
    """
    indices = input(
        "Enter stock index symbols separated by commas (e.g., ^GSPC, ^DJI): "
    ).split(",")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    plotter = StockExchangePerformancePlotter([index.strip() for index in indices])
    plotter.plot_performance(start_date, end_date)


def use_current_prices_ticker_display():
    """
    Utilizes CurrentPricesTickerDisplay to show a rolling display of current
    stock prices for a list of tickers.

    Users input stock tickers and a display interval, and the function
    continuously displays the current prices of these stocks in a ticker-like
    format.
    """
    tickers = input(
        "Enter stock ticker(s) separated by commas for current price display (e.g., AAPL, MSFT): "
    ).split(",")
    interval = int(input("Enter display interval in seconds: "))
    ticker_display = CurrentPricesTickerDisplay(
        [ticker.strip() for ticker in tickers], interval
    )
    ticker_display.display_ticker()


def main():
    """
    Main function to run the stock analysis application.

    Presents a menu-driven interface for users to select various stock analysis
    functionalities, including data fetching, plotting, and performance
    visualization. The script runs in a loop until the user chooses to exit.
    """
    while True:
        print("\nStock Data Analysis Menu")
        print("1. Use Stock Data Fetcher")
        print("2. Use Stock Summary Fetcher")
        print("3. Use Financial Metrics Fetcher")
        print("4. Use Revenue Growth Fetcher")
        print("5. Use Stock Price Plotter")
        print("6. Use Financial Metrics Plotter")
        print("7. Use Revenue Growth Plotter")
        print("8. Use Stock Volatility Plotter")
        print("9. Use Stock Exchange Performance Plotter")
        print("10. Use Current Prices Ticker Display")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            use_stock_data_fetcher()
        elif choice == "2":
            use_stock_summary_fetcher()
        elif choice == "3":
            use_financial_metrics_fetcher()
        elif choice == "4":
            use_revenue_growth_fetcher()
        elif choice == "5":
            use_stock_price_plotter()
        elif choice == "6":
            use_financial_metrics_plotter()
        elif choice == "7":
            use_revenue_growth_plotter()
        elif choice == "8":
            use_stock_volatility_plotter()
        elif choice == "9":
            use_stock_exchange_performance_plotter()
        elif choice == "10":
            use_current_prices_ticker_display()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
