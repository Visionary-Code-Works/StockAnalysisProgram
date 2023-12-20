# PowerShell script to create test directory structure

# Define the root directory for tests
$rootDir = "tests"

# Define subdirectories and corresponding Python files for testing
$subDirs = @{
    "test_fetcher" = @("test_financial_metrics_fetcher.py", "test_revenue_growth_fetcher.py", "test_stock_data_fetcher.py", "test_stock_summary_fetcher.py")
    "test_plotter" = @("test_current_prices_ticker_display.py", "test_financial_metrics_plotter.py", "test_revenue_growth_plotter.py", "test_stock_exchange_performance_plotter.py", "test_stock_price_plotter.py", "test_stock_volatility_plotter.py")
}

# Additions to the subDirs hash map
$subDirs["test_fetcher"] += "test_stock_data_fetcher.py"
$subDirs["."] = "test_main.py" # Creating test_main.py in the tests root


# Create the root directory if it does not exist
if (-not (Test-Path -Path $rootDir)) {
    New-Item -ItemType Directory -Path $rootDir
}

# Iterate over each subdirectory and create it with its test files
foreach ($subDir in $subDirs.Keys) {
    $fullSubDirPath = Join-Path -Path $rootDir -ChildPath $subDir

    # Create subdirectory
    if (-not (Test-Path -Path $fullSubDirPath)) {
        New-Item -ItemType Directory -Path $fullSubDirPath
    }

    # Create placeholder test files
    foreach ($file in $subDirs[$subDir]) {
        $fullFilePath = Join-Path -Path $fullSubDirPath -ChildPath $file

        if (-not (Test-Path -Path $fullFilePath)) {
            New-Item -ItemType File -Path $fullFilePath
        }
    }
}

Write-Host "Test directory structure created successfully."
