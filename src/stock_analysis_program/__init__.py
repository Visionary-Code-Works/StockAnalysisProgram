# src/__init__.py

from .fetcher import (
    StockDataFetcher,
    StockSummaryFetcher,
    FinancialMetricsFetcher,
    RevenueGrowthFetcher,
)
from .plotter import (
    StockPricePlotter,
    FinancialMetricsPlotter,
    RevenueGrowthPlotter,
    StockVolatilityPlotter,
    StockExchangePerformancePlotter,
    CurrentPricesTickerDisplay,
)
from .cli import main
from .exceptions import DataFetchError, StockAnalysisError

__all__ = [
    "StockDataFetcher",
    "StockSummaryFetcher",
    "FinancialMetricsFetcher",
    "RevenueGrowthFetcher",
    "StockPricePlotter",
    "FinancialMetricsPlotter",
    "RevenueGrowthPlotter",
    "StockVolatilityPlotter",
    "StockExchangePerformancePlotter",
    "CurrentPricesTickerDisplay",
    "DataFetchError",
    "StockAnalysisError",
    "main",
]
