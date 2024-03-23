import pandas as pd

# Creating a DataFrame with details of the finance APIs
finance_apis = pd.DataFrame(
    {
        "API Name": [
            "Alpha Vantage",
            "IEX Cloud",
            "Quandl",
            "Financial Modeling Prep",
            "World Trading Data",
            "MarketStack",
            "Finnhub",
            "Twelve Data",
        ],
        "Website": [
            "https://www.alphavantage.co",
            "https://iexcloud.io",
            "https://www.quandl.com",
            "https://financialmodelingprep.com",
            "https://www.worldtradingdata.com",
            "https://marketstack.com",
            "https://finnhub.io",
            "https://twelvedata.com",
        ],
        "Unique Feature": [
            "Wide range of data services; technical indicators",
            "Wide array of financial data; tiered pricing model with a free tier",
            "Financial, economic, and alternative data; free datasets available for academic use",
            "Broad set of financial data APIs; includes stock market data and financial statements",
            "Real-time and historical stock data; free tier available",
            "REST API interface to obtain stock market data from around the world; free tier with limited access",
            "Free APIs for stock data, forex, and crypto; both real-time and historical data",
            "Financial data including real-time and historical stock data, forex, and cryptocurrencies; free plan with limited access",
        ],
        "Pricing": [
            "Free/Paid",
            "Free/Paid",
            "Free/Paid",
            "Free/Paid",
            "Free/Paid",
            "Free/Paid",
            "Free/Paid",
            "Free/Paid",
        ],
    }
)

# Saving the DataFrame to a CSV file
file_path = "finance_apis.csv"
finance_apis.to_csv(file_path, index=False)
