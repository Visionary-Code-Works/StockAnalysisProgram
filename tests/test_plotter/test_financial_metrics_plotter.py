# tests/test_fetcher/test_financial_metrics_fetcher.py

from unittest.mock import patch
import pytest
import pandas as pd
from src.stock_analysis_program.plotter.financial_metrics_plotter import (
    FinancialMetricsPlotter,
)

# Adjust the sample data to be a DataFrame instead of a dict
sample_financial_data = pd.DataFrame(
    {
        "Ticker": ["AAPL", "MSFT"],
        "Market Cap": [1000000, 2000000],
        "PE Ratio": [25, 30],
        # Add more columns as needed
    }
)


@pytest.fixture
def mock_fetcher_return():
    """Fixture to mock the FinancialMetricsFetcher's return value as a DataFrame."""
    return sample_financial_data


@patch(
    "src.stock_analysis_program.plotter.financial_metrics_plotter.FinancialMetricsFetcher"
)
def test_financial_metrics_plotter(mock_FinancialMetricsFetcher, mock_fetcher_return):
    """Test the FinancialMetricsPlotter's plot_metrics method."""
    # Setup mock to return the sample financial data as a DataFrame
    mock_instance = mock_FinancialMetricsFetcher.return_value
    mock_instance.fetch_financial_metrics.return_value = mock_fetcher_return

    # Initialize the plotter with mock data
    plotter = FinancialMetricsPlotter(["AAPL", "MSFT"])

    with patch("matplotlib.pyplot.show"):
        plotter.plot_metrics()

    # Assert fetch_financial_metrics was called
    mock_instance.fetch_financial_metrics.assert_called_once()
