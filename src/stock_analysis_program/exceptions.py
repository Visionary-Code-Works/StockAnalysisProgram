"""Custom exceptions for stock_analysis_program."""


class StockAnalysisError(Exception):
    """Base exception for package-specific errors."""


class DataFetchError(StockAnalysisError):
    """Raised when a data provider returns no usable data."""
