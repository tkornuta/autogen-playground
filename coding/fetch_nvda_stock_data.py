# filename: fetch_nvda_stock_data.py

import yfinance as yf
import datetime

# Calculate the dates for the past month
today = datetime.datetime(2024, 6, 23)
start_date = today - datetime.timedelta(days=30)

# Fetching the NVIDIA stock data for the past month
nvidia_data = yf.download('NVDA', start=start_date, end=today)

# Printing relevant information
print(f"NVIDIA's stock data from {start_date.date()} to {today.date()}:\n")
print(nvidia_data[['Open', 'High', 'Low', 'Close', 'Volume']])