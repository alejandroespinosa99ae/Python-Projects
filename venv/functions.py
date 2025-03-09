
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

# Given the following strings, separate them into {{Ticker Name: GAP}, {Company: The Gap, Inc.}, {Increased: 3.67}, {Percent Increased: 18.84}
# 

#GAP The Gap, Inc.  23.15 +3.67 (+18.84%)
#LB LandBridge Company LLC  67.72 +6.21 (+10.10%)
#RGTI Rigetti Computing, Inc.  9.35 +0.84 (+9.87%)
#ELF e.l.f. Beauty, Inc.  70.68 +6.26 (+9.72%)
#TGTX TG Therapeutics, Inc.  38.44 +3.25 (+9.24%)

#
#
s = "LB LandBridge Company LLC  67.72 +6.21 (+10.10%)"
print("s has a size of : ", len(s), "    can you select a character from the string like an array? ", s.find("("))
def description_spliter(desc_list): # input will be a list of strings
   # create an empty dictionary
   dictionary_of_stock_info = {}
   #tempList = {"name", "company", "price", "gain", "percent"}
   for s in desc_list:
       # to get the percent
       position = s.find("(")
       percent = s[position:].strip() #"(+10.10%)"
        
        # to remove everything in between "(   )" technically after "("
       s = s.replace(percent,"") #"LB LandBridge Company LLC  67.72 +6.21 "
        
        # to get the text that includes "+" and everything after until the end of the string
       position = s.find("+")
       gain = s[position:].strip() #"+6.21"

        # to remove "+" and everthing after
       s = s.replace(gain,"") #"LB LandBridge Company LLC  67.72 "
        
        # to get the ticker name
       position = s.find(" ")
       name = s[0:position].strip() #"LB"
       
        # to keep the text after the ticker name
       s = s.replace(name,"").strip() #" LandBridge Company LLC  67.72 "
        
        # reversing the string to make it easier to get the stock price 
       s_reversed = s[::-1] #" 27.76  CLL ynapmoC egdirBdnaL"
        
       position = s_reversed.find(" ")
       price_reversed = s_reversed[:position] #"27.76"
        
       price = price_reversed[::-1] #"67.72"
       s_reversed = s_reversed.replace(price_reversed,"") #" LandBridge Company LLC  "
       company = s_reversed[::-1].strip() #"LandBridge Company LLC"
       
       dictionary_of_stock_info["name"] = name
       dictionary_of_stock_info["company"] = company
       dictionary_of_stock_info["price"] = price
       dictionary_of_stock_info["gain"] = gain
       dictionary_of_stock_info["percent"] = percent
       
   return(dictionary_of_stock_info)

   
""" example_dictionary = {}
list_str = ["a","b"]
counter = 0
for s in list_str:
    example_dictionary[s] = counter
    counter = counter + 1

print("this is my example dictionary:",example_dictionary) """
#
###########description_spliter(s)
##string_to_num("GAP")

def test_list(list_of_strings):
    """ for string_ in list_of_strings:
        position = string_.find("(")
        percent = string_[position:].strip()
        print(f"percent is: {percent}") """
    for s in list_of_strings:
        position = s.find("(")
        percent = s[position:].strip()
        print("percent: ", percent)

        s = s.replace(percent,"")
        print("s is : ", s)
        position = s.find("+")
        gain = s[position:].strip()
        s = s.replace(gain,"")
        print("s is : ", s, " and gain is: ", gain)
        position = s.find(" ")
        name = s[0:position].strip()
        s = s.replace(name,"").strip()
        print("s is : ", s, " name is: ", name)
        print(f"The string  {s},  will be reversed to:  {s[::-1]}")
        s_reversed = s[::-1]
        print(f"the blank position is in {s_reversed.find(" ")}")
        position = s_reversed.find(" ")
        price_reversed = s_reversed[:position]
        print(f"price_reversed is: {price_reversed}")
        price = price_reversed[::-1]
        s_reversed = s_reversed.replace(price_reversed,"")
        s = s_reversed[::-1].strip()
        print(f"s is now {s} and the price is {price}")

testing_strings_ = ["GAP The Gap, Inc.  23.15 +3.67 (+18.84%)","LB LandBridge Company LLC  67.72 +6.21 (+10.10%)"]
test_list(testing_strings_)
print(description_spliter(testing_strings_))
#

# https://www.reddit.com/r/LearnUselessTalents/comments/avb5bi/how_do_i_learn_to_calculate_the_day_of_the_week/
# Date format is YYYY-MM-DD
def day_of_week(date):
    day = int(date[8:])
    leap_year_modifier = is_leap_year(date)
    week_day = (year_code(date) + month_code(date) + century_code(date) + day -leap_year_modifier)%7
    #print("Year code is: ", year_code(date), " month code is ", month_code(date), " century code is: ", century_code(date), " day is: ", day, " leap year modifier is: ", leap_year_modifier)
    return week_day

# Function to determine if leap year
def is_leap_year(year):
    year = year[0:4] # this will create a substring for the year in format YYYY
    year = int(year)
    if (year % 4 == 0):
        if((year % 100 == 0) and (year % 400 != 0)):
            return 0#False
        else:
            return 1#True
    else:
        return 0#False
    
def month_code(date):
    month = date[5:7]
    code = 0
    if((is_leap_year(date) == True) and (month == "01")):
        return 0
    elif((is_leap_year(date) == True) and (month == "04")):
        return 3
    else:
        if(month == "01"):
            code = 0
        elif(month == "02"):
            code = 3
        elif(month == "03"):
            code = 3
        elif(month == "04"):
            code = 6
        elif(month == "05"):
            code = 1
        elif(month == "06"):
            code = 4
        if(month == "07"):
            code = 6
        elif(month == "08"):
            code = 2
        elif(month == "09"):
            code = 5
        elif(month == "10"):
            code = 0
        elif(month == "11"):
            code = 3
        elif(month == "12"): # was else but it wasnt working? it was giving wrong month_code
            code = 5
    return code

def year_code(date):
    year = int(date[2:4])
    return (year + int((year/4)))% 7  

def century_code(date): # if 19th century
    if(date[0:2] == "19"):
        return 0
    else: # if 20th century
        return 6

def day_number(date):
    day = date[8]
    if(day == "0"):
        return int(date[9])
    else:
        return int(date[8:])
    
""" testDate = "2025-03-08"
#testDate = "1969-12-20"
testDate = "2001-08-25"
print("This is the number for the day of the week " ,day_of_week(testDate))
 """