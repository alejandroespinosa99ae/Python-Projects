
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
#

# Date format is YYYY-MM-DD
def day_of_week(date):
    day = int(date[8:])
    leap_year_modifier = is_leap_year(date)
    week_day = (year_code(date) + month_code(date) + century_code(date) + day -leap_year_modifier)%7
    #print("Year code is: ", year_code(date), " month code is ", month_code(date), " century code is: ", century_code(date), " day is: ", day, " leap year modifier is: ", leap_year_modifier)
    return week_day

"""     # Determine if the year is a leap year
    if(is_leap_year(date) == True):
        year_code(date) + month_code(date) + century_code(date) + day -leap_year_modifier
    else: # If not a leap year """



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
    
testDate = "2025-03-08"
#testDate = "1969-12-20"
testDate = "2001-08-25"
print("This is the number for the day of the week " ,day_of_week(testDate))
