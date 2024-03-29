# Documentation for Stock Analysis Program

[![Upload Python Package](https://github.com/Visionary-Code-Works/stock-analysis-program/actions/workflows/python_publish.yml/badge.svg)](https://github.com/Visionary-Code-Works/stock-analysis-program/actions/workflows/python_publish.yml)

- [Home](../README.md)
- [Workflow](./Workflow.md)
- [Plotter](./Plotter.md)
- [Fetcher](./Fetcher.md)

## Overview

This stock analysis program comprises several Python classes designed to fetch and visualize various financial data and metrics related to stocks. The program is modular, allowing easy integration of its components into larger financial analysis systems or applications.

## Components

The program contains two main types of classes: Fetchers and Plotters.

### Fetchers

[Link to detailed notes](./Fetcher.md)

1. **StockDataFetcher**: Fetches historical stock data, moving averages, average trading volume, and key financial metrics for a given stock ticker.
2. **StockSummaryFetcher**: Retrieves summary information for multiple stock tickers, including name, sector, industry, and key financial data.
3. **FinancialMetricsFetcher**: Gathers financial metrics such as market cap, P/E ratio, and profit margins for a list of stock tickers.
4. **RevenueGrowthFetcher**: Calculates year-over-year revenue growth for multiple stock tickers.

### Plotters

[Link to detailed notes](./Plotter.md)

1. **StockPricePlotter**: Visualizes stock prices and moving averages.
2. **FinancialMetricsPlotter**: Plots histograms of financial metrics for a list of stocks.
3. **RevenueGrowthPlotter**: Visualizes year-over-year revenue growth in a bar chart format.
4. **StockVolatilityPlotter**: Plots rolling volatility for stock tickers.
5. **StockExchangePerformancePlotter**: Compares performance of various stock indices by plotting normalized closing prices.
6. **CurrentPricesTickerDisplay**: Displays current stock prices in a dynamic, ticker-like format.

## Usage

```mermaid
flowchart LR
    A{{Start Application}} --> B((Main Menu))
    B --> C{Exit}
    B --> D([Use Stock Data Fetcher])
    B --> E([Use Stock Summary Fetcher])
    B --> F([Use Financial Metrics Fetcher])
    B --> G([Use Revenue Growth Fetcher])
    B --> H([Use Stock Price Plotter])
    B --> I([Use Financial Metrics Plotter])
    B --> J([Use Revenue Growth Plotter])
    B --> K([Use Stock Volatility Plotter])
    B --> L([Use Stock Exchange\nPerformance Plotter])
    B --> M([Use Current Prices\nTicker Display])

    D --> N[[Enter Stock Ticker]]
    E --> O[[Enter Stock Tickers]]
    F --> P[[Enter Stock Tickers\nfor Financial Metrics]]
    G --> Q[[Enter Stock Tickers\nfor Revenue Growth]]
    H --> R[[Enter Stock Tickers\nand Date Range\nfor Price Plotting]]
    I --> S[[Enter Stock Tickers\nfor Financial Metrics Plotting]]
    J --> T[[Enter Stock Tickers\nfor Revenue Growth Plotting]]
    K --> U[[Enter Stock Tickers\nand Date Range\nfor Volatility Plotting]]
    L --> V[[Enter Stock Index Symbols\nand Date Range]]
    M --> W[[Enter Stock Tickers\nand Display Interval]]

    N --> B
    O --> B
    P --> B
    Q --> B
    R --> B
    S --> B
    T --> B
    U --> B
    V --> B
    W --> B
```

### Fetchers-a

Each fetcher class can be used independently to retrieve specific data. For example:

```python
from fetcher.stock_summary_fetcher import StockSummaryFetcher

# Fetching stock summaries
summary_fetcher = StockSummaryFetcher(['AAPL', 'MSFT'])
summaries = summary_fetcher.get_summaries()
print(summaries)
```

### Plotters-a

Plotters are used for visualizing data. They often depend on fetchers to get the necessary data. For example:

```python
from plotter.stock_price_plotter import StockPricePlotter

# Plotting stock prices
price_plotter = StockPricePlotter(['AAPL', 'MSFT'])
price_plotter.plot_closing_prices('2021-01-01', '2021-12-31')
```

### Integration

To integrate these classes into a larger program:

1. **Import Classes**: Import the necessary classes from their respective modules.
2. **Fetch Data**: Use fetcher classes to retrieve the required data.
3. **Visualize Data**: Use plotter classes to visualize the fetched data.
4. **Combine Logic**: Create functions or classes that combine the logic of fetching and plotting for streamlined operations.

## Extending the Program

To extend the program:

- **Add New Fetchers/Plotters**: Implement new classes for additional types of data fetching and visualization.
- **Enhance Existing Classes**: Add more features, such as different types of plots or additional financial metrics.

## Example Integration

Here's an example of how to integrate multiple components in a larger program:

```python
from fetcher.revenue_growth_fetcher import RevenueGrowthFetcher
from plotter.revenue_growth_plotter import RevenueGrowthPlotter

def plot_revenue_growth(tickers):
    # Fetching revenue growth
    growth_fetcher = RevenueGrowthFetcher(tickers)
    growth_data = growth_fetcher.fetch_revenue_growth()

    # Plotting revenue growth
    growth_plotter = RevenueGrowthPlotter(tickers)
    growth_plotter.plot_revenue_growth()

# Example usage
plot_revenue_growth(['AAPL', 'MSFT', 'GOOGL'])
```

This documentation provides a comprehensive overview of the program's structure, usage, and potential for integration and extension. It can be adapted to fit the specific requirements of any financial analysis tool or system.
