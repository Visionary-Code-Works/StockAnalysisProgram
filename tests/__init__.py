# tests/__init__.py

from .test_fetcher import (
    test_financial_metrics_fetcher,
    test_revenue_growth_fetcher_initialization,
    test_stock_data_fetcher,
    test_stock_summary_fetcher_initialization
)
from .test_plotter import (
    test_current_prices_ticker_display_initialization,
    test_financial_metrics_plotter,
    test_revenue_growth_plotter_initialization,
    test_stock_exchange_performance_plotter,
    test_stock_price_plotter_initialization,
    test_stock_volatility_plotter_initialization
)
from .test_main import test_main_exists
