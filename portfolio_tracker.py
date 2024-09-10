# importing yfinance library for real-time stock data
import yfinance


# Creating the Portfolio class with two attributes:
# Owner which contains the owner's Full Name and Portfolio which is a dictionary of symbol:quantity

class Portfolio:
    # defining the constructor with default values
    def __init__(self, Owner='', symbol_quantity={}):
        self.Owner = Owner
        self.__portfolio = symbol_quantity  # Corrected typo to __portfolio

    # implementing a getter for the portfolio because it is a private attribute
    def get_portfolio(self):
        return self.__portfolio

    # implementing the add_stock function to add a stock to the portfolio
    def add_stock(self, symbol, quantity):
        if symbol not in self.__portfolio:
            self.__portfolio[symbol] = quantity  # Add stock if it doesn't exist
        else:
            self.__portfolio[symbol] += quantity  # Update the quantity if it exists
        print(f"Added {quantity} of {symbol} to the portfolio.")

    # implementing remove_stock function to remove a stock from the portfolio
    def remove_stock(self, symbol):
        if symbol not in self.__portfolio:
            print('This Stock has not been registered yet.')
            return
        self.__portfolio.pop(symbol)
        print(f"Removed {symbol} from the portfolio.")

    # implementing the function that counts one stock value
    def getStockvalue(self, symbol):
        if symbol not in self.__portfolio:
            print('This Stock has not been registered yet.')
            return 'NONE'
        stock = yfinance.Ticker(symbol)
        return stock.info['currentPrice'] * self.__portfolio[symbol]

    # implementing the function that counts all the portfolio's value
    def getTotalvalue(self):
        return sum([self.getStockvalue(symbol) for symbol in self.__portfolio])

    # implementing the function to get the stock's current price
    def get_StockCurrentPrice(self, symbol):
        stock = yfinance.Ticker(symbol)
        return stock.info['currentPrice']


# Implementing the Test code:
answer = input('Do you want to create a portfolio (y/n): ')
if answer.lower() != 'y':
    print('Okay Bye!')
    exit()

Owner = input('Write your full name: ')
TestP = Portfolio(Owner)

print("Great, you have created your first portfolio. Do you want to: ")
while True:
    answer = input(
        "\n1-Add a stock.\n2-Remove a stock.\n3-Get a stock value.\n4-Get your portfolio's total value.\n5-Get a current stock price.\nChoose an option: ")

    match int(answer):
        case 1:
            Symbol = input('Please type the symbol of the stock: ')
            Quantity = input('Please type the quantity of shares: ')
            TestP.add_stock(Symbol, int(Quantity))
        case 2:
            Symbol = input('Please type the symbol of the stock: ')
            TestP.remove_stock(Symbol)
        case 3:
            Symbol = input('Please type the symbol of the stock: ')
            print('The total value you have in this stock is: ', TestP.getStockvalue(Symbol))
        case 4:
            print('The total value of your portfolio is: ', TestP.getTotalvalue())
        case 5:
            Symbol = input('Please type the symbol of the stock: ')
            print('The current price of this stock is: ', TestP.get_StockCurrentPrice(Symbol))

    answer = input('Do you want to continue? (y/n): ')
    if answer.lower() != 'y':
        print('Your portfolio has been updated successfully.')
        break
