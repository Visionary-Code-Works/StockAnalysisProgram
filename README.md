# Stock Analysis Program

[![Upload Python Package](https://github.com/Visionary-Code-Works/StockAnalysisProgram/actions/workflows/python_publish.yml/badge.svg)](https://github.com/Visionary-Code-Works/StockAnalysisProgram/actions/workflows/python_publish.yml)

## Overview

The Stock Analysis Program is a Python-based toolkit designed to fetch and visualize financial data and metrics for stocks. It is ideal for financial analysts, traders, and anyone interested in stock market analysis. The program offers functionalities such as retrieving historical stock data, computing moving averages, analyzing revenue growth, and plotting financial metrics.

## Features

- **Data Fetching**: Retrieve historical data, financial summaries, and key metrics for stocks.
- **Data Visualization**: Visualize stock prices, financial metrics, and revenue growth.
- **Comparative Analysis**: Compare performance of different stocks and stock indices.
- **Customizability**: Modular design allows for easy customization and extension.

## Installation

Install the package from PyPI:

```bash
pip install stock-analysis-program
```

The package also installs a small command-line menu:

```bash
stock-analysis
```

## Usage

The program consists of multiple Python classes categorized into Fetchers and Plotters.

### Fetchers

- `StockDataFetcher`
- `StockSummaryFetcher`
- `FinancialMetricsFetcher`
- `RevenueGrowthFetcher`

### Plotters

- `StockPricePlotter`
- `FinancialMetricsPlotter`
- `RevenueGrowthPlotter`
- `StockVolatilityPlotter`
- `StockExchangePerformancePlotter`
- `CurrentPricesTickerDisplay`

### Example

```python
from stock_analysis_program import StockPricePlotter

# Plotting stock prices for Apple and Microsoft
price_plotter = StockPricePlotter(['AAPL', 'MSFT'])
price_plotter.plot_closing_prices('2021-01-01', '2021-12-31')
```

Plotter methods return Matplotlib figure and axes objects for notebook,
testing, or dashboard usage:

```python
figures = price_plotter.plot_closing_prices(
    '2021-01-01',
    '2021-12-31',
    show=False,
)
```

## Documentation

For detailed documentation on each component, please refer to the `docs` directory.

- [Workflow](./docs/Workflow.md)
- [Plotter](./docs/Plotter.md)
- [Fetcher](./docs/Fetcher.md)
- [Documentation](./docs/documentation.md)

## Contributing

Contributions to enhance the program are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
