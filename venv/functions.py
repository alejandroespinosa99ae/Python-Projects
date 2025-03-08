
# function to return the ticker name given the stockInfo
def ticker_name(stockInfo):
    l = []
    for x in stockInfo:
        c = x.text().strip()
        space = c.find(" ")
        ticker = c[:space]
        l.append(ticker)
    return l

# In order to use .history, the tickers must a string of tickers, so we need to convert the list to a string
        
def list_to_string(list):
    tempString = " " # define the start of the string
    for item in list: 
        tempString = tempString + " " + str(item)
        print("what type is the current item has type: ",item)
    return tempString.lstrip()