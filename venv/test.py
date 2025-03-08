import yfinance as yf
import time
import csv

# Define the stock ticker (e.g., Apple: AAPL)
ticker = "AAPL"


""" stock = yf.Ticker(ticker)
price = stock.history(period="1d")['Close'].iloc[-1]  # Get the latest close price
print(f"Current price of {ticker}: ${price:.2f}")

stockData = stock.history(period="1d", interval="5m")# gets the data for 
print (stockData)
#time.sleep(300)  # Wait for 5 minutes (300 seconds)

#stockData.to_csv("APPL_stockData.csv") """

tickers = ["AAPL", "GOOG"]
data = yf.download(tickers,start="2025-03-07", period="1d",interval ="5m")
print(data)
#data.to_csv("testdata.csv")