####################################################
#   Notes: The STOCKHISTORY fucntion is only available 
#   in certain versions of Excel. To replicate this in 
#   Python the yfinance library can be used. The idea for 
#   this project came from not having access to the STOCKHISTORY 
#   function in Excel
#
####################################################

# Import libraries
import httpx
from selectolax.parser import HTMLParser

url = "https://finance.yahoo.com"
# To access the web
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0"}

# Information that the website gives will be stored in the following variable
resp = httpx.get(url, headers=headers)
# Parse raw HTML to use for querying
html = HTMLParser(resp.text)

print(html.css_first("title").text())



### testing yfinance

import yfinance as yf
import pandas as pd

ticker = "AAPL"
start_date = "2025-01-01"
end_date = "2025-03-03"

stock_data = yf.download(ticker, start = start_date, end = end_date)

#print(data)

# OPTIONAL save as csv file
# data.to_csv("stock_data.csv")









