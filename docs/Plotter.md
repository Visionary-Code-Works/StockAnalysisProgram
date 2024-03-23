# Plotter

[Home](../README.md)
[Workflow](./Workflow.md)
[Fetcher](./Fetcher.md)
[Documentation](./documentation.md)

## Overview

The `plotter` package facilitates the visualization of financial and stock market data. It is designed to assist traders, investors, financial analysts, and anyone interested in market trends, financial performance, and risk assessment through graphical representations.

### Classes

- `CurrentPricesTickerDisplay`
- `FinancialMetricsPlotter`
- `RevenueGrowthPlotter`
- `StockExchangePerformancePlotter`
- `StockPricePlotter`
- `StockVolatilityPlotter`

---

## CurrentPricesTickerDisplay

### Description

Displays current stock prices in a ticker-like format for real-time monitoring.

### Initialization

```python
CurrentPricesTickerDisplay(tickers, interval=10)
```

#### Parameters

- `tickers` (list of str): List of stock ticker symbols.
- `interval` (int, optional): Update interval in seconds. Default is 10 seconds.

### Methods

#### fetch_current_prices

Fetches current prices for the stock tickers.

##### Returns

- `dict`: Current prices of the tickers.

#### display_ticker

Displays the current prices in a rolling ticker format.

---

## FinancialMetricsPlotter

### Description

Plots financial metrics of stocks in a histogram format for comparison.

### Initialization

```python
FinancialMetricsPlotter(tickers)
```

#### Parameters

- `tickers` (list of str): Stock tickers for financial metrics plotting.

### Methods

#### plot_metrics

Plots histograms of various financial metrics.

---

## RevenueGrowthPlotter

### Description

Visualizes year-over-year revenue growth of stocks in a bar chart format.

### Initialization

```python
RevenueGrowthPlotter(tickers)
```

#### Parameters

- `tickers` (list of str): Stock tickers for revenue growth plotting.

### Methods

#### plot_revenue_growth

Plots year-over-year revenue growth.

---

## StockExchangePerformancePlotter

### Description

Compares and visualizes the performance of different stock indices over time.

### Initialization

```python
StockExchangePerformancePlotter(indices)
```

#### Parameters

- `indices` (list of str): Stock index symbols for performance comparison.

### Methods

#### plot_performance

Plots normalized closing prices of the indices for comparison.

---

## StockPricePlotter

### Description

Visualizes stock prices and their moving averages over a selected period.

### Initialization

```python
StockPricePlotter(tickers)
```

#### Parameters

- `tickers` (list of str): Stock tickers for price visualization.

### Methods

#### plot_closing_prices

Plots the closing prices of the stocks.

#### plot_moving_averages

Plots moving averages along with closing prices.

---

## StockVolatilityPlotter

### Description

Calculates and visualizes the rolling volatility of stock prices.

### Initialization

```python
StockVolatilityPlotter(tickers)
```

#### Parameters

- `tickers` (list of str): Stock tickers for volatility analysis.

### Methods

#### plot_volatility

Calculates and plots rolling volatility.
