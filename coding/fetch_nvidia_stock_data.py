# filename: fetch_nvidia_stock_data.py
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    # Fetch historical stock data
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Nvidia ticker symbol is NVDA
ticker_symbol = "NVDA"
# Define the time frame
start_date = '2024-07-01'
end_date = '2024-08-01'

# Fetch the data
nvidia_data = fetch_stock_data(ticker_symbol, start_date, end_date)

# Print the fetched data
print(nvidia_data)
