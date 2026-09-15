inventory = 0

while True:
    stock = input("Enter a stock quantity (or 'quit'): ")

    if stock == "quit":
        break

    if not stock.isdigit():
        print("Invalid input")
        continue