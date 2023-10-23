#DATA VISUALISATION TOOLS (Matplotlib and Seaborn) = PART 2
#Basic plotting for financial Data
import matplotlib.pyplot as plt
import seaborn as sns

stock_price=[100,102,104,103,105,107,108]
dates=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
plt.figure(figsize=(10,6))
sns.lineplot(x=dates,y=stock_price)
plt.title("Stock price over a week")
plt.xlabel("Days")
plt.ylabel("Stock Price")
plt.grid(True)
#plt.show()

#Exercise 1: Plotting Stock Prices using Matplotlib
#CHALLENGE
import matplotlib.pyplot as plt
import seaborn as sns
stock_price=[105,103,106,109,108,107,110,112,111,113]
stock_price_2=[107,108,107,107,106,108,109,110,109,111]
plt.figure(figsize=(10,10))
plt.plot(stock_price,color='green',label='Stock 1')
plt.plot(stock_price_2,color='red',label='Stock 2')
plt.title("Stock price over 10 days")
plt.xlabel("Dates")
plt.ylabel("Stock price")
plt.grid(True)
plt.legend()
#plt.show()

#Exercise 2: Visualizing Distributions using Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
stock_return=[0.05,-0.02,0.03,-0.01,0.02,0.03,-0.03,0.01,0.04,-0.01]
plt.figure(figsize=(10,4))
sns.lineplot(x=list(range(1,11)),y=stock_return)
plt.title('Distribution of Stock Returns')
plt.xlabel('days')
plt.ylabel('Stock Returns')
plt.grid(True)
plt.show()
#Correction
import matplotlib.pyplot as plt
import seaborn as sns
returns = [0.05, -0.02, 0.03, -0.01, 0.02, 0.03, -0.03, 0.01, 0.04, -0.01]
sns.histplot(returns, bins=5, kde=True) 
'''L'argument bins dans la fonction histplot vous permet de spécifier combien de ces intervalles vous souhaitez pour votre histogramme.
KDE est une méthode pour estimer la fonction de densité de probabilité d'une variable aléatoire continue.'''
plt.title('Distribution of Stock Returns')
plt.show()

