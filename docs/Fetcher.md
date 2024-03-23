# Fetchers

[Home](../README.md)
[Workflow](./Workflow.md)
[Plotter](./Plotter.md)
[Documentation](./documentation.md)

## Overview

The `fetcher` package is designed for financial data retrieval and analysis. It includes classes for fetching financial metrics, revenue growth, stock data, and stock summaries from Yahoo Finance using the `yfinance` library. This package is suitable for investors, financial analysts, traders, and anyone interested in performing detailed stock market research and analysis.

### Classes

- `FinancialMetricsFetcher`
- `RevenueGrowthFetcher`
- `StockDataFetcher`
- `StockSummaryFetcher`

---

| Class / Initialization                                           | Description                                                                                                                                                                                                                                         | Methods                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| FinancialMetricsFetcher </br> `FinancialMetricsFetcher(tickers)` | Retrieves important financial metrics for a list of stock tickers, including:<br> market capitalization, P/E ratio, forward P/E, price to book ratio, and profit margins.<br> Ideal for financial analysis and comparisons across different stocks. | **`fetch_financial_metrics`**: Fetches and compiles financial metrics for each ticker in the list.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Returns**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `pandas.DataFrame`: A DataFrame containing the financial metrics for each ticker.                                                                                                                                                                                                                                                                                                      |
| RevenueGrowthFetcher </br> `RevenueGrowthFetcher(tickers)`       | Fetches and calculates the year-over-year revenue growth for a list of stock tickers.<br> Utilizes historical financial data to assess company performance over time.                                                                               | **`fetch_revenue_growth`**: Calculates the most recent year-over-year revenue growth for each ticker.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Returns**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `dict`: A dictionary with tickers as keys and their respective year-over-year revenue growth percentages as values.                                                                                                                                                                                                                                                                 |
| StockDataFetcher </br> `StockDataFetcher(ticker)`                | Fetches various types of stock data, including: historical data, moving averages,<br> average trading volume, and key financial metrics.                                                                                                            | **`fetch_historical_data`**: Retrieves historical stock data for the specified period.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Parameters**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `period` (str, optional): The time period for which to fetch the data. Defaults to '1y'.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Returns**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `pandas.DataFrame`: Historical stock data.<br><br>**`calculate_moving_averages`**: Calculates moving averages for given window sizes.<br><br>**`get_average_volume`**: Calculates the average trading volume.<br><br>**`get_financial_metrics`**: Fetches and returns key financial metrics. |
| StockSummaryFetcher </br> `StockSummaryFetcher(tickers)`         | Fetches and provides summary information for a list of stock tickers, including:<br> company name, sector, industry, and key financial metrics.                                                                                                     | **`fetch_summary`**: Fetches summary information for a given stock ticker.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Parameters**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `ticker` (str): The stock ticker.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Returns**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `dict`: Summary information of the stock.<br><br>**`get_summaries`**: Retrieves stock summaries for all tickers specified during initialization.<br>&nbsp;&nbsp;&nbsp;&nbsp;**Returns**<br>&nbsp;&nbsp;&nbsp;&nbsp;- `list of dict`: Summaries for each stock ticker.                                                                                                                                     |

---

## FinancialMetricsFetcher

### Description

Retrieves important financial metrics for a list of stock tickers, including market capitalization, P/E ratio, forward P/E, price to book ratio, and profit margins. Ideal for financial analysis and comparisons across different stocks.

### Initialization

```python
FinancialMetricsFetcher(tickers)
```

#### Parameters

- `tickers` (list of str): A list of stock ticker symbols (e.g., `['AAPL', 'MSFT']`) for which financial metrics are to be fetched.

### Methods

#### fetch_financial_metrics

Fetches and compiles financial metrics for each ticker in the list.

##### Returns

- `pandas.DataFrame`: A DataFrame containing the financial metrics for each ticker.

---

## RevenueGrowthFetcher

### Description

Fetches and calculates the year-over-year revenue growth for a list of stock tickers. Utilizes historical financial data to assess company performance over time.

### Initialization

```python
RevenueGrowthFetcher(tickers)
```

#### Parameters

- `tickers` (list of str): Stock tickers to fetch the revenue growth for.

### Methods

`fetch_revenue_growth`: Calculates the most recent year-over-year revenue growth for each ticker.

Returns

- `dict`: A dictionary with tickers as keys and their respective year-over-year revenue growth percentages as values.

---

## StockDataFetcher

### Description

Fetches various types of stock data, including historical data, moving averages, average trading volume, and key financial metrics.

### Initialization

```python
StockDataFetcher(ticker)
```

#### Parameters

- `ticker` (str): The stock ticker symbol for which the data is to be fetched.

### Methods

#### fetch_historical_data

Retrieves historical stock data for the specified period.

##### Parameters

- `period` (str, optional): The time period for which to fetch the data. Defaults to '1y'.

##### Returns

- `pandas.DataFrame`: Historical stock data.

#### calculate_moving_averages

Calculates moving averages for given window sizes.

##### Parameters

- `data` (pandas.DataFrame): The historical stock data.
- `window_sizes` (list of int, optional): Window sizes for calculating moving averages. Defaults to `[20, 50, 200]`.

##### Returns

- `dict`: Moving averages for each window size.

#### get_average_volume

Calculates the average trading volume.

##### Parameters

- `data` (pandas.DataFrame): The historical stock data.

##### Returns

- `float`: Average trading volume.

#### get_financial_metrics

Fetches and returns key financial metrics for the stock.

##### Returns

- `dict`: Key financial metrics.

---

## StockSummaryFetcher

### Description

Fetches and provides summary information for a list of stock tickers, including company name, sector, industry, and key financial metrics.

### Initialization

```python
StockSummaryFetcher(tickers)
```

#### Parameters

- `tickers` (str or list of str): The stock ticker(s) for which the summary information is to be fetched.

### Methods

#### fetch_summary

Fetches summary information for a given stock ticker.

##### Parameters

- `ticker` (str): The stock ticker.

##### Returns

- `dict`: Summary information of the stock.

#### get_summaries

Retrieves stock summaries for all tickers specified during initialization.

##### Returns

- `list of dict`: Summaries for each stock ticker.
