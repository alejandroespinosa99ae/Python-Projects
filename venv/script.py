# Import libraries
import httpx
from selectolax.parser import HTMLParser

url = "https://en.wikipedia.org/wiki/Lists_of_earthquakes#Deadliest_earthquakes"
# To access the web
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0"}

# Information that the website gives will be stored in the following variable
resp = httpx.get(url, headers=headers)
# Parse raw HTML to use for querying
html = HTMLParser(resp.text)

print(html.css_first("title").text())








