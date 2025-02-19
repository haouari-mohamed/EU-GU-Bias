import requests
import pandas as pd
from analysis import calculate_correlation, calculate_fvg, calculate_bias

# Replace 'your_api_key' with your actual Alpha Vantage API key
API_KEY = 'your_api_key'


# Fetch data from Alpha Vantage API for EUR/USD and GBP/USD
def fetch_data():
    url_eurusd = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=EUR&to_symbol=USD&apikey={API_KEY}&outputsize=full'
    url_gbpusd = f'https://www.alphavantage.co/query?function=FX_DAILY&from_symbol=GBP&to_symbol=USD&apikey={API_KEY}&outputsize=full'

    # Fetch data for EUR/USD and GBP/USD
    response_eurusd = requests.get(url_eurusd)
    response_gbpusd = requests.get(url_gbpusd)

    # Convert the response to JSON and then to a pandas DataFrame
    eurusd_data = response_eurusd.json()
    gbpusd_data = response_gbpusd.json()

    # Extract the 'Time Series FX (Daily)' data and convert to DataFrame
    eurusd_df = pd.DataFrame.from_dict(eurusd_data['Time Series FX (Daily)'], orient='index')
    gbpusd_df = pd.DataFrame.from_dict(gbpusd_data['Time Series FX (Daily)'], orient='index')

    # Ensure the data is in a datetime format and sorted
    eurusd_df.index = pd.to_datetime(eurusd_df.index)
    gbpusd_df.index = pd.to_datetime(gbpusd_df.index)

    # Sort the data by date (ascending)
    eurusd_df = eurusd_df.sort_index()
    gbpusd_df = gbpusd_df.sort_index()

    # Only keep 'close' prices (or whatever you need)
    eurusd_df = eurusd_df[['4. close']].rename(columns={'4. close': 'Close'})
    gbpusd_df = gbpusd_df[['4. close']].rename(columns={'4. close': 'Close'})

    return eurusd_df, gbpusd_df


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
