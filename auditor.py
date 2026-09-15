inventory = 0

while True:
    stock = input("Enter a stock quantity (or 'quit'): ")

    if stock == "quit":
        break

    elif not stock.isdigit():
        print("Invalid input")
        continue

    else:
        stock = int(stock)

    inventory += stock

    if inventory > 500:
        print("Overstock Alert!")
        break