#1. FINANCIAL TIME SERIES (Forecasting, Risk management, Decision making)
#EXERCISE 1: Write a Python function to calculate the average stock price over these days.
dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]
average_price=0
for dates, stock_prices in zip(dates,stock_prices):
    average_price= stock_prices/3+average_price
print(average_price)
#Correction:
dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]
def calculate_average(prices):
    return sum(prices)/len(prices)
average_price=calculate_average(stock_prices)
print(f"Average Stock Price: ${average_price}")

#EXERCISE 2: Write a Python function to find the day with the highest stock price.
dates = ["4th January", "5th January", "6th January"]
stock_prices = [155, 156, 153]
def highest_stock_price(dates, stock_prices):
    """
    Returns the day with the highest stock price.
    
    Args:
    - dates (list): List of days.
    - stock_prices (list): List of stock prices corresponding to the days.
    
    Returns:
    - str: The day with the highest stock price.
    """
    # Find the index of the maximum stock price
    max_index = stock_prices.index(max(stock_prices))
    # Return the corresponding date
    return dates[max_index]
print("The highest stock price is", highest_stock_price(dates, stock_prices))  # Outputs: '5th January'

#EXERCISE 3: Write a Python function to determine if the stock prices are generally increasing, decreasing, or remaining stable.
dates.extend(["7th January", "8th January"]) # Extend the data
stock_prices.extend([157, 152]) # Extend the data
def stock_trend(dates,stock_prices):
    increasing= all(stock_prices[i]<stock_prices[i+1] for i in range(len(stock_prices)-1))
    decreasing= all(stock_prices[i]>stock_prices[i+1] for i in range(len(stock_prices)-1))
    if increasing:
        return "increasing"
    elif decreasing:
        return "decreasing"
    else:
        return "stable"
print(stock_trend(dates,stock_prices))

#2. Exercises related to ”Importance of Time Series in Finance”

#EXERCISE 1: Write a Python function to calculate the volatility (standard deviation) of the selected stock prices.
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
stock_prices = [150, 152, 151, 153, 152]
import statistics
def calculate_volatility(prices):
    return statistics.stdev(prices)
volatility=calculate_volatility(stock_prices)
print(f"Volatility: ${volatility:.2f}")

#EXERCISE 2:  Write a Python function to calculate the average stock price and highlight days when the stock price is above the average.
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
stock_prices = [150, 152, 151, 153, 152]
def above_average_days(dates,prices):
    # Calculate average stock price
    average_price = sum(prices) / len(prices)
    # Identify days where stock price is above the average
    above_avg_days=[date for i, date in enumerate(dates) if prices[i]>average_price]
    return average_price, above_avg_days
# Call the function
avg_price, highlighted_days = above_average_days(dates, stock_prices)
print(f"Average Stock Price: ${avg_price:.2f}")
print(f"Days with stock price above average: {', '.join(highlighted_days)}")

#EXERCICE 3: Write a Python function to forecast the next day’s stock price based on the average increase or decrease of the previous days.
dates = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
stock_prices = [150, 152, 151, 153, 152]
def forecast_next_day(stock_prices):
    #Calculate the daily differences
    daily_diffs=[stock_prices[i] - stock_prices[i-1] for i in range(1,len(stock_prices))]
    #Calculate the average of the differences
    avg_diff=sum(daily_diffs)/len(daily_diffs)
    #Forecastthe next day's stock price
    forecast=stock_prices[-1]+avg_diff
    return forecast
forecasted_price=forecast_next_day(stock_prices)
print(f"Forecasted price for the next day: ${forecasted_price:.2f}")

#3. TIME VALUE OF MONEY
#PRESENT VALUE
#EXERCISE 1: Given a future value of $120, an interest rate of 5%, and a period of 2 years, calculate the present value.
def present_value(FV,r,n):
        return FV/(1+r)**n
FV=120
r=0.05
n=2
PV=present_value(FV,r,n)
print(f"Present value is: ${PV:.2f}")

#EXERCISE 2: Suppose you’re expecting $500 two years from now. If the discount rate is 6%, what is this amount worth today?
def present_value(FV,r,n):
    return FV/(1+r)**n
FV=500
r=0.06
n=2
PV=present_value(FV,r,n)
print(f"$500 is worth ${PV:.2f} today")

#EXERCISE 3: How much would a sum of $1000 due 5 years from now be worth today if the interest rate is 4%?
def present_value(FV,r,n):
    return FV/(1+r)**n
FV=1000
r=0.04
n=5
PV=present_value(FV,r,n)
print(f"A sum of $1000 due 5 years from now would be worth ${PV:.2f} today")

#FUTURE VALUE
#EXERCISE 1: If you invest $90 today at an interest rate of 7% for a period of 1 year, how much will you have at the end of the year?
def future_value(PV,r,n):
    return PV*(1+r)**n
PV=90
r=0.07
n=1
FV=future_value(PV,r,n)
print(f"The FV would be ${FV:.2f}")

#EXERCISE 2: If you place $200 in a savings account that offers a 3% interest rate compounded annually, how much will you have in the account after 2 years?
def future_value(pv,r,n):
    return pv*(1+r)**n
PV=200
r=0.03
n=2
FV=future_value(PV,r,n)
print(f"Exercise 2: ${FV:.2f}")

#EXERCISE 3:Given an initial investment of $150 and an annual interest rate of 5%, how much will the investment be worth after 3 years?
def future_value(pv,r,n):
    return pv*(1+r)**n
PV=150
r=0.05
n=3
FV=future_value(PV,r,n)
print(f"Exercise 3: ${FV:.2f}")

#Exercises related to ”Discounting and Compounding”
#EXERCISE 1: If you put $80 in a bank that offers a 9% annual interest rate, how much will you have after compounding for one year?
def compound(pv,r):
    return pv*(1+r)
PV=80
r=0.09
FV=compound(PV,r)
print(f"Exercise 1: ${FV:.2f}")

#EXERCISE 2:Calculate the present value of $115 that you are to receive one year from now, given an interest rate of 8%.
def discount_value(FV,r):
    return FV/(1+r)
FV=115
r=0.08
PV=discount_value(FV,r)
print(f"Exercise 2: ${PV:.2f}")

#EXERCISE 3: How much do you need to invest today to ensure you have $500 after two years if the annual interest rate is 6%?
def discounting(fv,r,n):
    return fv/(1+r)**n
FV=500
r=0.06
n=2
PV=discounting(FV,r,n)
print(f"Exercise 3: ${PV:.2f}")

#EXERCISE 4: If you are promised $180 two years from now and the discount rate is 10%, what is the value of that promise today?
def discount_value(fv,r,n):
    return fv/(1+r)**n
FV=180
r=0.1
n=2
PV=discount_value(FV,r,n)
print(f"Exercise 4: ${PV:.2f}")

#EXERCISE 5: Suppose you can invest money at 7% per annum. How much do you need to invest now to ensure that you will have $1000 three years from now?
def present_value(fv,r,n):
    return fv/(1+r)**n
FV=1000
r=0.07
n=3
PV=present_value(FV,r,n)
print(f"Exercise 5: ${PV:.2f}")

#4. Working with Time Series Data using pandas

#4.1 Fetching Data from Yahoo Finance
import yfinance as yf
# Download Apple stock data
apple_data = yf.download("AAPL", start="2020-01-01", end="2023-01-01")
# Display the first few rows of the data
print(apple_data.head())

#4.2 Working with Time Series Data

#Plotting th closing price:
import matplotlib.pyplot as plt
apple_data["Close"].plot(figsize=(10, 5))
plt.title("Apple Stock Closing Prices")
plt.ylabel("Price (in \$)")
plt.xlabel("Date")
plt.show()

#Calculating Moving average:
apple_data["50-day MA"]= apple_data["Close"].rolling(window=50).mean()
apple_data[["Close","50-day MA"]].plot(figsize=(10,5))
plt.title("Apple Stock Prices with 50-day Moving Average")
plt.ylabel("Price (in \$)")
plt.xlabel("Date")
plt.show()

#Resampling:
weekly_data = apple_data["Close"].resample("W").mean()
weekly_data.plot(figsize=(10, 5))
plt.title("Apple Stock Weekly Closing Prices")
plt.ylabel("Price (in \$)")
plt.xlabel("Date")
plt.show()

#Exercises for Working with Time Series Data using pandas:

#EXERCISE 1: Fetch the daily stock data of Microsoft (ticker: ”MSFT”) for the year 2021.
microsoft_data=yf.download("MSFT", start="2021-01-01", end="2021-12-31")
print(microsoft_data.head())

#EXERCISE 2: Retrieve the historical stock price data of Google (ticker: ”GOOGL”) from January 1, 2020, to December 31, 2022.
google_data=yf.download("GOOGL",start="2020-01-01",end="2022-12-31")
print(google_data.head())

#EXERCISE 3: How would you fetch the stock data of Amazon (ticker: ”AMZN”) for the last quarter of 2021?
amazon_data=yf.download("AMZN",start="2021-10-01", end="2021-12-31")
print(amazon_data.head())

#Exercises related to ”Plotting the closing prices”:
#EXERCISE 1: Plot the daily closing prices of Tesla Inc. (ticker: ”TSLA”) for the year 2020.
tesla_data=yf.download("TSLA",start="2020-01-01",end="2020-12-31")
tesla_data["Close"].plot(figsize=(10,5))
plt.title("Tesla Stock CLosing Prices 2020")
plt.ylabel("Stock closing price (in /$)")
plt.xlabel("Date")
plt.show()

#EXERCISE 2: How would you visualize the daily closing prices of Netflix (ticker: ”NFLX”) for the first half of 2022?
netflix_data=yf.download("NFLX",start="2022-01-01",end="2022-06-30")
netflix_data["Close"].plot(figsize=(10,5))
plt.title("Netflix Stock CLosing Prices 2020")
plt.ylabel("Stock closing price (in /$)")
plt.xlabel("Date")
plt.show()

#EXERCISE 3: Generate a plot showcasing the daily closing prices of Facebook (ticker:”FB”) for the entire year of 2019.
fb_data=yf.download("META",start="2019-01-01",end="2019-12-31")
fb_data["Close"].plot(figsize=(10,5))
plt.title("Facebook Stock Closing Price 2019")
plt.ylabel("Price (in /$)")
plt.xlabel("Date")
plt.show()

#Exercises related to ”Calculating moving averages”:
#EXERCISE 1: Calculate and plot a 30-day moving average on top of the daily closing prices of IBM (ticker: ”IBM”) for 2020.
ibm_data=yf.download("IBM",start="2020-01-01",end="2020-12-31")
ibm_data["30-Day MA"]=ibm_data["Close"].rolling(window=30).mean()
ibm_data[["Close","30-Day MA"]].plot(figsize=(10,5))
plt.title=("30-day moving average IBM price")
plt.ylabel("Price (in /$)")
plt.xlabel("Date")
plt.show()

#EXERCISE 2: Overlay a 20-day moving average on the daily closing prices of Adobe Systems (ticker: ”ADBE”) for the year 2021.
adobe_data=yf.download("ADBE",start="2021-01-01",end="2021-12-31")
adobe_data["20-day MA"]=adobe_data["Close"].rolling(window=20).mean()
adobe_data[["Close","20-day MA"]].plot(figsize=(10,5))
plt.title=("20-day moving average Adobe Systems daily closing price")
plt.ylabel("Price (in /$)")
plt.xlabel("Date")
plt.show()

#EXERCISE 3: For Nvidia Corporation (ticker: ”NVDA”) in 2022, visualize the daily closing prices along with its 40-day moving average.
nvidia_data=yf.download("NVDA",start="2022-01-01",end="2022-12-31")
nvidia_data["40-day MA"]=nvidia_data["Close"].rolling(window=40).mean()
nvidia_data[["Close","40-day MA"]].plot(figsize=(10,5))
plt.ylabel("Price (in /$)")
plt.xlabel("Date")
plt.show()

#Exercises related to ”Resampling”:
#EXERCISE 1:Resample the daily closing prices of Starbucks Corp. (ticker: ”SBUX”) in 2020 to get monthly average closing prices.
starbucks_data=yf.download("SBUX",start="2020-01-01",end="2020-12-31")
monthly_data=starbucks_data["Close"].resample("M").mean()
monthly_data.plot(figsize=(10,5))
plt.ylabel("Price (in \$)")
plt.xlabel("Date")
plt.show()

#EXERCISE 2: Resample the daily closing prices of Disney (ticker: ”DIS”) in 2019 to show bi-weekly (every two weeks) average closing prices.
disney_data=yf.download("DIS",start="2019-01-01",end="2019-12-31")
biweekly_data=disney_data["Close"].resample("2W").mean()
biweekly_data.plot(figsize=(10,5))
plt.ylabel("Price (in \$)")
plt.xlabel("Date")
plt.show()

#EXERCISE 3: For Coca-Cola Company (ticker: ”KO”) in 2020, how would you derive and plot the quarterly average closing prices?
coca_data=yf.download("KO",start="2020-01-01",end="2020-12-31")
quarterly_data=coca_data["Close"].resample("Q").mean()
quarterly_data.plot(figsize=(10,5))
plt.ylabel("Price (in /$)")
plt.xlabel("Date")
plt.show()