# Live_Crypto_Data_Analyser

I developed this Crypto Data Analyser is a Python project that fetches, analyses, and presents real-time data for the top 50 cryptocurrencies by market cap using the CoinGecko API. It collects key metrics like price, market cap, volume, and 24-hour changes, updating the data every 5 minutes in an Excel sheet for easy access and analysis.

## Key Features
- **Live Data Fetching**: Retrieve live cryptocurrency data from the CoinGecko API.
- **Real-Time Analysis**:
  - Identify the top 5 cryptocurrencies by market capitalization.
  - Calculate the average price of the top 50 cryptocurrencies.
  - Analyze the highest and lowest 24-hour percentage price changes.
- **Dynamic Excel Sheet**: Updates an Excel file every 5 minutes with the latest data, making it easy to track cryptocurrency trends.

## Technologies Used
- **Python 3.x**
- **API**: CoinGecko API
- **Libraries**:
  - `requests`
  - `pandas`
  - `openpyxl`
    
- Install the required dependencies:
    ``` bash pip install -r requirements.txt```
- Run the Python script to start fetching and analyzing live cryptocurrency data:
    ```  bash python crypto_python_script.py```





