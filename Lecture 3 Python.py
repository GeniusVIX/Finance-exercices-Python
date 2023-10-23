
#Exercise 1: Stocks and dividends
class Stock:
    def __init__(self, name, price, dividend):
        self.name = name
        self.price = price
        self.dividend = dividend
    
    def yield_dividend(self):
        return self.dividend / self.price
applestock = Stock('Apple', 150, 0.82)
print(applestock.yield_dividend())

#Exercise 2: Finanial instrument portfolio
class Portfolio:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, instrument):
        if isinstance(instrument, Stock):  # Ensure we're adding valid stocks
            self.instruments.append(instrument)
        else:
            print(f"{type(instrument).__name__} is not a valid financial instrument.")

    def total_value(self):
        return sum(instrument.price for instrument in self.instruments)  
portfolio = Portfolio()
portfolio.add_instrument(Stock('Apple', 150, 0.82))
portfolio.add_instrument(Stock('Microsoft', 220, 1.2))
print(portfolio.total_value())  # 150 + 220 = 370

#Exercise 3: Currency Converter tool
class CurrencyConverter:
    def __init__(self):
        # Nested dictionary to hold conversion rates.
        # Example: {'USD': {'EUR': 0.85, 'JPY': 110.0}, 'EUR': {'USD': 1.18}}
        self.rates = {}

    def add_rate(self, source_currency, target_currency, rate):
        """Adds a conversion rate for a given currency pair."""
        if source_currency not in self.rates:
            self.rates[source_currency] = {}
        self.rates[source_currency][target_currency] = rate

    def convert(self, amount, source_currency, target_currency):
        """Converts a given amount from the source currency to the target currency."""
        if source_currency not in self.rates or target_currency not in self.rates[source_currency]:
            raise ValueError(f"Conversion rate for {source_currency} to {target_currency} not available.")
        return amount * self.rates[source_currency][target_currency]
# Example usage:
converter = CurrencyConverter()
# Adding some sample conversion rates
converter.add_rate('USD', 'EUR', 0.85)
converter.add_rate('USD', 'JPY', 110.0)
converter.add_rate('EUR', 'USD', 1.18)
# Converting 100 USD to EUR
converted_amount = converter.convert(100, 'USD', 'EUR')
print(f"100 USD is equal to {converted_amount} EUR")  # Expected: 85.0 EUR

#MATHEMATICAL TOOLS WITH NUMPY
import numpy as np
prices = np.array([100, 102, 104, 101, 99, 98])
returns = (prices[1:]-prices[:-1])/prices[:-1]
print("Daily returns:", returns)
# Assuming 252 trading days
annual_volatility = np.std(returns) * np.sqrt(252)
print("Annualized volatility:", annual_volatility)

#Exercise 1: Stock Price simulation with Numpy
import numpy as np
np.random.seed(0) #For reproducibility
daily_returns=np.random.normal(0.001, 0.02, 1000)
stock_prices=[100]
for r in daily_returns:
    stock_prices.append(stock_prices[-1]*(1+r))
print(stock_prices[-1]) 
"""Ce code simule l'évolution du prix d'un actif sur 1000 jours en se basant sur des rendements quotidiens générés aléatoirement,
puis il affiche le prix de l'actif à la fin de cette période."""

#Exercise 2: Portfolio Variance
import numpy as np
stddev1=0.1
stddev2=0.2
corrcoef=0.5
w1, w2=0.6, 0.4 
var=(w1**2*stddev1**2)+(w2**2*stddev2**2)+(2*w1*w2*stddev1*stddev2*corrcoef)
print("La variance est ", var)

#Exercise 3: Efficient Frontier
import numpy as np
return_A, return_B=0.10, 0.15 #Annual Return Asset A et B
sigma_A, sigma_B=0.2, 0.3 #Annual Volatility Asset A et B
rho_AB=0 #Assuming no correlation for simplicity
def portfolio_return(w_A,w_B):
    """Calculate portfolio return for given weights"""
    return w_A*return_A+w_B*return_B
def portfolio_volatility(w_A,w_B,rho=rho_AB):
    """Calculate portfoliovolatility for given weights and correlation"""
    return np.sqrt(w_A**2*sigma_A**2+w_B**2*sigma_B**2+2*w_A*w_B*sigma_A*sigma_B*rho)
weights=[(0,1),(0.1,0.9),(0.7,0.3)]#Creation d'un sample de weights combinations
for w_A,w_B in weights:
    print(f"Weight A: {w_A:.1f}, Weight B: {w_B:.1f}")
    print(f"Portfolio Return: {portfolio_return(w_A, w_B)*100:.2f}%")
    print(f"Portfolio Volatility: {portfolio_volatility(w_A, w_B)*100:.2f}%")
    print("------")