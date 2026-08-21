stock_prices = {
    "Apple": 180,
    "Tesla": 250,
    "Google": 150,
    "Amazon": 170,
    "Microsoft": 400
}

stock_name = input("Enter stock name: ")
quantity = int(input("Enter quantity: "))

if stock_name in stock_prices:
    price = stock_prices[stock_name]
    total_investment = price * quantity

    print("Stock Price:", price)
    print("Total Investment:", total_investment)
else:
    print("Stock not found.")