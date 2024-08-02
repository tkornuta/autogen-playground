# filename: plot_stocks.py
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from datetime import datetime

# Set the start and end date for YTD
start_date = '2024-01-01'
today_date = '2024-08-01'

# Fetch stock data for NVDA and TSLA
nvda_data = web.DataReader('NVDA', 'yahoo', start_date, today_date)
tsla_data = web.DataReader('TSLA', 'yahoo', start_date, today_date)

# Calculate the percentage gain from the first trading day of 2024
nvda_gain = (nvda_data['Close'][-1] / nvda_data['Close'][0] - 1) * 100
tsla_gain = (tsla_data['Close'][-1] / tsla_data['Close'][0] - 1) * 100

# Create a bar plot for the YTD gains of NVDA and TSLA
plt.figure(figsize=(8, 6))
plt.bar(['NVDA', 'TSLA'], [nvda_gain, tsla_gain], color=['blue', 'green'])
plt.ylabel('Percentage Gain (%)')
plt.title('YTD Stock Gains for NVDA and TSLA as of 2024-08-01')
plt.grid(True)

# Save the plot to a file
plt.savefig('ytd_stock_gains.png')
plt.show()