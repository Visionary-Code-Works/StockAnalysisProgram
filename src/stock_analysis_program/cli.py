"""Command-line interface for stock_analysis_program."""

from .fetcher import (
    FinancialMetricsFetcher,
    RevenueGrowthFetcher,
    StockDataFetcher,
    StockSummaryFetcher,
)
from .plotter import (
    CurrentPricesTickerDisplay,
    FinancialMetricsPlotter,
    RevenueGrowthPlotter,
    StockExchangePerformancePlotter,
    StockPricePlotter,
    StockVolatilityPlotter,
)


def _parse_tickers(prompt):
    return [ticker.strip().upper() for ticker in input(prompt).split(",") if ticker.strip()]


def use_stock_data_fetcher():
    ticker = input("Enter a stock ticker (e.g., AAPL, GOOGL): ").strip().upper()
    fetcher = StockDataFetcher(ticker)
    historical_data = fetcher.fetch_historical_data()
    moving_averages = fetcher.calculate_moving_averages(historical_data)
    average_volume = fetcher.get_average_volume(historical_data)
    financial_metrics = fetcher.get_financial_metrics()

    print(f"Moving Averages for {ticker}: {moving_averages}")
    print(f"Average Volume for {ticker}: {average_volume}")
    print(f"Financial Metrics for {ticker}: {financial_metrics}")


def use_stock_summary_fetcher():
    tickers = _parse_tickers("Enter stock ticker(s) separated by commas (e.g., GOOGL, AAPL): ")
    fetcher = StockSummaryFetcher(tickers)
    summaries = fetcher.get_summaries()

    for summary in summaries:
        print(f"\nSummary for {summary['Ticker']}:\n")
        for key, value in summary.items():
            print(f"{key}: {value if value is not None else 'N/A'}")


def use_financial_metrics_fetcher():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for financial metrics (e.g., AAPL, MSFT): "
    )
    fetcher = FinancialMetricsFetcher(tickers)
    print("\nFinancial Metrics:")
    print(fetcher.fetch_financial_metrics())


def use_revenue_growth_fetcher():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for revenue growth (e.g., AAPL, MSFT): "
    )
    fetcher = RevenueGrowthFetcher(tickers)
    revenue_growth = fetcher.fetch_revenue_growth()

    print("\nYear-over-Year Revenue Growth:")
    for ticker, growth in revenue_growth.items():
        print(f"{ticker}: {growth:.2%}" if growth is not None else f"{ticker}: Data not available")


def use_stock_price_plotter():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for price plotting (e.g., AAPL, MSFT): "
    )
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    plotter = StockPricePlotter(tickers)
    plotter.plot_closing_prices(start_date, end_date)
    plotter.plot_moving_averages(start_date, end_date)


def use_financial_metrics_plotter():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for financial metrics plotting (e.g., AAPL, MSFT): "
    )
    FinancialMetricsPlotter(tickers).plot_metrics()


def use_revenue_growth_plotter():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for revenue growth plotting (e.g., AAPL, MSFT): "
    )
    RevenueGrowthPlotter(tickers).plot_revenue_growth()


def use_stock_volatility_plotter():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for volatility plotting (e.g., AAPL, MSFT): "
    )
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    StockVolatilityPlotter(tickers).plot_volatility(start_date, end_date)


def use_stock_exchange_performance_plotter():
    indices = _parse_tickers(
        "Enter stock index symbols separated by commas (e.g., ^GSPC, ^DJI): "
    )
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    StockExchangePerformancePlotter(indices).plot_performance(start_date, end_date)


def use_current_prices_ticker_display():
    tickers = _parse_tickers(
        "Enter stock ticker(s) separated by commas for current price display (e.g., AAPL, MSFT): "
    )
    interval = int(input("Enter display interval in seconds: "))
    CurrentPricesTickerDisplay(tickers, interval).display_ticker()


def main():
    actions = {
        "1": use_stock_data_fetcher,
        "2": use_stock_summary_fetcher,
        "3": use_financial_metrics_fetcher,
        "4": use_revenue_growth_fetcher,
        "5": use_stock_price_plotter,
        "6": use_financial_metrics_plotter,
        "7": use_revenue_growth_plotter,
        "8": use_stock_volatility_plotter,
        "9": use_stock_exchange_performance_plotter,
        "10": use_current_prices_ticker_display,
    }

    while True:
        print(
            "\nStock Data Analysis Menu\n"
            "1. Use Stock Data Fetcher\n"
            "2. Use Stock Summary Fetcher\n"
            "3. Use Financial Metrics Fetcher\n"
            "4. Use Revenue Growth Fetcher\n"
            "5. Use Stock Price Plotter\n"
            "6. Use Financial Metrics Plotter\n"
            "7. Use Revenue Growth Plotter\n"
            "8. Use Stock Volatility Plotter\n"
            "9. Use Stock Exchange Performance Plotter\n"
            "10. Use Current Prices Ticker Display\n"
            "0. Exit\n"
        )

        choice = input("Enter your choice: ")
        if choice == "0":
            break

        action = actions.get(choice)
        if action is None:
            print("Invalid choice. Please try again.")
            continue

        try:
            action()
        except Exception as exc:
            print(f"Error: {exc}")
