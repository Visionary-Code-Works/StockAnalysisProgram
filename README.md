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

To use this program, ensure you have Python installed on your system. Clone this repository and install the required dependencies:

```bash
git clone https://github.com/visionary-code-works/stock-analysis-program.git
cd stock-analysis-program
pip install -r requirements.txt
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
from plotter.stock_price_plotter import StockPricePlotter

# Plotting stock prices for Apple and Microsoft
price_plotter = StockPricePlotter(['AAPL', 'MSFT'])
price_plotter.plot_closing_prices('2021-01-01', '2021-12-31')
```

## Documentation

For detailed documentation on each component, please refer to the `docs` directory.

[Workflow](./docs/Workflow.md)
[Plotter](./docs/Plotter.md)
[Fetcher](./docs/Fetcher.md)
[Documentation](./docs/documentation.md)

## Contributing

Contributions to enhance the program are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
