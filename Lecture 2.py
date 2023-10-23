#Exercice 1.3
stocks=["AAPL","MSFT","GOOGL"]
stocks.append("IBM")
print(stocks)

#Exercice 1.4
stocks=["TSLA","AMZN","FB"]
stocks.extend(["NVDA","AMD"])
print(stocks)

#Exercice 1.5
stocks_details={
"ticker":"AAPL",
"opening_price":142.7,
"closing_price":143.2,
"volume":1200000
}
print(stocks_details)

#Exercice 1.6
bond={
    "issuer":"AAPL",
    "maturity date":"09/12/2023",
    "coupon rate":"4%",
    "face value":124
}
print(bond)

#EXERCICE LOOP
#Exo 1
stock=[105,107,104,106,103]
daily_returns=[]
for i in range(1, len(stock)):
    daily_return=(stock[i]-stock[i-1])/stock[i-1]
    daily_returns.append(daily_return)
    print(daily_return)

#Exo 2
average_return=sum(daily_returns)/len(daily_returns)
print("Average return is", average_return)

#Exo 3
principal=500
rate=0.07
years=0
while principal<1000:
    principal*=(1+rate)
    years+=1
print(years)

#Exo 4
principal=500
rate=0.07
years=0
while principal<1000:
    principal*=(1+rate)
    years+=1
print(years,"Final value",principal)

#CONDITIONAL STATEMENTS
#Exercice 1
bond_yield=0.038
if bond_yield>4:
    print("Buy the bond")
else:
    print("Don't buy the bond")

#Exercice 2
bond_yield=0.038
if bond_yield>=0.04:
    print("Buy the bond")
else:
    print("Don't buy the bond")

#Exercice 3
PE_ratio=17
if PE_ratio>=17:
    print("sell the stock")
elif PE_ratio<10:
    print("buy the stock")
else:
    print("Hold the stock")

#Exercice 4
PE_ratio=14
if 27>=PE_ratio>=23:
    print("Sell the stock")
elif 16>=PE_ratio>=14:
    print("Buy the stock")
else:
    print("Hold the stock")