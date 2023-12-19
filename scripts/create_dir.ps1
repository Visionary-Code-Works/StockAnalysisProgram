# PowerShell Script to create the file structure

# Define the directory names
$rootDir = "StockAnalysisApp"
$fetchersDir = "Fetchers"
$plottersDir = "Plotters"

# Define the file names
$fetcherFiles = @("stock_data_fetcher.py", "stock_summary_fetcher.py", "financial_metrics_fetcher.py", "revenue_growth_fetcher.py")
$plotterFiles = @("stock_price_plotter.py", "financial_metrics_plotter.py", "revenue_growth_plotter.py", "stock_volatility_plotter.py", "stock_exchange_performance_plotter.py", "current_prices_ticker_display.py")
$mainFile = "main.py"

# Create the root directory
New-Item -ItemType Directory -Force -Path $rootDir

# Create subdirectories
New-Item -ItemType Directory -Force -Path "$rootDir\$fetchersDir"
New-Item -ItemType Directory -Force -Path "$rootDir\$plottersDir"

# Create fetcher files
foreach ($file in $fetcherFiles) {
    New-Item -ItemType File -Force -Path "$rootDir\$fetchersDir\$file"
}

# Create plotter files
foreach ($file in $plotterFiles) {
    New-Item -ItemType File -Force -Path "$rootDir\$plottersDir\$file"
}

# Create the main file
New-Item -ItemType File -Force -Path "$rootDir\$mainFile"

# Output the structure
Get-ChildItem -Recurse $rootDir
