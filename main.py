import yfinance as yf
import pandas as pd
from analysis import calculate_correlation, calculate_fvg, calculate_bias

# Fetch historical data for EUR/USD and GBP/USD
def fetch_data():
    eurusd = yf.download('EURUSD=X', start='2020-01-01', end='2025-01-01', interval='1d')
    gbpusd = yf.download('GBPUSD=X', start='2020-01-01', end='2025-01-01', interval='1d')
    return eurusd, gbpusd

# Main function
def main():
    eurusd, gbpusd = fetch_data()

    # Calculate correlation between EUR/USD and GBP/USD
    correlation = calculate_correlation(eurusd, gbpusd)
    print(f"Correlation between EUR/USD and GBP/USD: {correlation}")

    # Identify FVGs for EUR/USD and GBP/USD
    eurusd_fvg = calculate_fvg(eurusd)
    gbpusd_fvg = calculate_fvg(gbpusd)
    print(f"FVG in EUR/USD: {eurusd_fvg}")
    print(f"FVG in GBP/USD: {gbpusd_fvg}")

    # Determine the daily bias
    bias = calculate_bias(correlation, eurusd_fvg, gbpusd_fvg)
    print(f"Daily Bias: {bias}")

if __name__ == '__main__':
    main()
