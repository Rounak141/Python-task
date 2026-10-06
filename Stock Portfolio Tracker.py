stocks = {
   "RELIANCE": 1200.00,
    "TCS": 3200.00,
    "INFY": 1500.00,
    "SBIN": 800.00,
    "ITC": 450.00,
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 170.00,
    "MSFT": 420.00

}

print("\nAvailable stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)

total_investment = 0
mylist = {}

while True:
        
    stock = input("Enter stock or 'EXIT' to quit :").upper()
    if stock == "EXIT":
        print("Exiting the program.")
        break 
    elif stock in stocks:
        while True:
            try:
                quantity = int(input("Enter quantity :"))
                if quantity <= 0:
                    print("Error: Quantity must be greater than zero.")
                    continue
                break
            except ValueError:
                print("Error: Please enter a valid integer for quantity.")
        price = stocks[stock]
        total = price * quantity
        total_investment = total_investment + total
        if stock in mylist:
            mylist[stock] = mylist[stock] + quantity
        else:
            mylist[stock] = quantity

        print("Investment in", stock, "=", total)

    else:
        print("Error: enter valid Stock name from the list.")
    
print("\n====Stock Portfolio Summary")

for stock, quantity in mylist.items():

    price = stocks[stock]
    investment = price * quantity

    print("Stock:", stock)
    print("Quantity:", quantity)
    print("Investment:", investment)
    print()

        
print("Total investment =", total_investment)


with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("=======================\n")

    for stock, quantity in mylist.items():
        price = stocks[stock]
        investment = price * quantity

        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Investment: {investment:.2f}\n\n")

    file.write(f"Total Investment: {total_investment:.2f}\n")

print("Portfolio saved to portfolio.txt")
