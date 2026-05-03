"""Internal helpers shared by fetchers and plotters."""

from .exceptions import DataFetchError


def normalize_tickers(tickers):
    if isinstance(tickers, str):
        tickers = [tickers]

    normalized = [str(ticker).strip().upper() for ticker in tickers if str(ticker).strip()]
    if not normalized:
        raise ValueError("At least one ticker symbol is required.")

    return normalized


def require_columns(data, columns, context):
    missing = [column for column in columns if column not in data.columns]
    if data.empty or missing:
        detail = "empty data" if data.empty else f"missing columns: {', '.join(missing)}"
        raise DataFetchError(f"No usable data returned for {context} ({detail}).")
