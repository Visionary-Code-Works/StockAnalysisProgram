# tests/test_fetcher/test_financial_metrics_fetcher.py

from unittest.mock import patch
import pytest
from src.stock_analysis_program import FinancialMetricsPlotter

# Sample data to simulate fetch_financial_metrics return value
sample_financial_data = {
    "Ticker": ["AAPL", "MSFT"],
    "Market Cap": [1000000, 2000000],
    "PE Ratio": [25, 30],
    # Add more sample financial metrics if needed
}


@pytest.fixture
def mock_fetcher_return():
    """Fixture to mock the FinancialMetricsFetcher's return value."""
    return sample_financial_data


# Note: Adjust the patch target to match how FinancialMetricsFetcher is
# imported within FinancialMetricsPlotter
@patch("src.stock_analysis_program.FinancialMetricsFetcher")
def test_financial_metrics_plotter(mock_FinancialMetricsFetcher, mock_fetcher_return):
    """Test the FinancialMetricsPlotter's plot_metrics method."""

    # Setup mock to return the sample financial data
    mock_instance = mock_FinancialMetricsFetcher.return_value
    mock_instance.fetch_financial_metrics.return_value = mock_fetcher_return

    # Initialize the plotter with mock data
    plotter = FinancialMetricsPlotter(["AAPL", "MSFT"])

    # Due to the nature of plotting, we mainly verify the interaction with the fetcher
    # and ensure no exceptions are raised during plotting
    with patch("matplotlib.pyplot.show") as mock_show:
        plotter.plot_metrics()

        # Assert fetch_financial_metrics was called
        mock_instance.fetch_financial_metrics.assert_called_once()

        # Verify plt.show was called, implying that plotting was attempted
        assert (
            mock_show.called
        ), "Expected plt.show to be called, indicating that plotting was attempted."
