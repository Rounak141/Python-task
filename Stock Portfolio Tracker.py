stocks = {
    "AAPL":180,
    "TSLA":250,
    "GOOG":150,
}
while True:
    stock = input("Enter stock :").upper()
    if stock == "EXIT":
        print("Exiting the program.")
        break 
    elif stock in stocks:
        quantity = int(input("Enter quantity :"))
        price = stocks[stock]
        total = price * quantity
        print("Total investment =", total)

    else:
        print("Error:Stock not found!")