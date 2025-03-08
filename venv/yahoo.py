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
# Import the functions I made
from functions import ticker_name, list_to_string

url = "https://finance.yahoo.com"
# To access the web
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0"}

# Information that the website gives will be stored in the following variable
resp = httpx.get(url, headers=headers)
# Parse raw HTML to use for querying
html = HTMLParser(resp.text)

ListGainers = [] # List of the top Gainers
List_stock_info = []

# Find the list with the topGainers and store it
ul_element = html.css_first('li[data-id="TopGainers"] ul') # Select the first matching <ul>

if ul_element:
    li_elements = ul_element.css("li")  # Get all <li> elements inside <ul>
    
    for li in li_elements:
        print(li.text().strip())  # Print text of each <li>
        ListGainers.append(li)
        List_stock_info.append(li.text().strip())


print("\n")
print(ticker_name(ListGainers), "    ", list_to_string(ticker_name(ListGainers)))
print('\n')
ListTickers = ticker_name(ListGainers)

# Find the list with the topLosers and store it
ul_element = html.css_first('li[data-id="TopLosers"] ul')#("ul.dock.yf-pmz4k")  # Select the first matching <ul>

if ul_element:
    li_elements = ul_element.css("li")  # Get all <li> elements inside <ul>
    
    for li in li_elements:
        print(li.text().strip())  # Print text of each <li>

### testing yfinance

import yfinance as yf
from datetime import datetime as date
import csv

#ticker = ["AAPL", "TNXP"]
start_date = date.today().strftime('%Y-%m-%d') # todays date in YYYY-MM-DD format
folder_path = 'Top Gainers/'

stock_data = yf.download(ListTickers, start = start_date, period="1d", interval="5m") # 
stock_data.to_csv(f"{folder_path}.csv")
List_stock_info.to_csv("StockInfo.csv")

    

