# -*- coding: utf-8 -*-
"""Crypto python script.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1stvmbJe9-wWMqTJShBefJX0NPPdIthCI
"""

from google.colab import drive
drive.mount('/content/drive')

pip install requests pandas openpyxl

import requests
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import time

def fetch_cryptocurrency_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def analyze_data(data):
    df = pd.DataFrame(data)
    df = df[['name', 'symbol', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']]

    # Analysis
    top_5_market_cap = df.nlargest(5, 'market_cap')
    avg_price = df['current_price'].mean()
    highest_change = df.loc[df['price_change_percentage_24h'].idxmax()]
    lowest_change = df.loc[df['price_change_percentage_24h'].idxmin()]

    insights = {
        "Top 5 by Market Cap": top_5_market_cap,
        "Average Price": avg_price,
        "Highest Change (24h)": highest_change,
        "Lowest Change (24h)": lowest_change
    }
    return df, insights

def update_excel(dataframe, file_name="/content/drive/MyDrive/crypto_data.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.title = "Crypto Data"

    for row in dataframe_to_rows(dataframe, index=False, header=True):
        ws.append(row)

    wb.save(file_name)

def main():
    file_name = "/content/drive/MyDrive/crypto_data.xlsx"
    print("Starting data fetch and analysis...")

    while True:
        try:
            # Fetch data
            data = fetch_cryptocurrency_data()

            # Analyze data
            df, insights = analyze_data(data)

            # Update Excel
            update_excel(df, file_name)

            print(f"Updated {file_name} with latest data. Next update in 5 minutes...")
            print(f"Insights:\n{insights}\n")

            # Wait for 5 minutes before updating again
            time.sleep(300)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(300)

if __name__ == "__main__":
    main()