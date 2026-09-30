# inventory = 0
failed_entries = 0
transaction_history = []

def load_inventory():
    try:
        file = open("inventory.txt", "r")
        inventory = int(file.readline())
        file.close()
        return inventory
    except FileNotFoundError:
        return 0

inventory = load_inventory()

def get_valid_input():
    stock = input("Enter a stock quantity (or 'quit'): ")

    if stock == "quit":
        return "quit"

    elif stock.isdigit():
        return int(stock)

    else:
        print("Invalid input")
        return None

# result = get_valid_input()
# print(result)



def process_delivery(current_total, new_value):
    updated_total = new_value + current_total
    return updated_total

# delivery = process_delivery(400,150)
# print(delivery)



def calculate_tax(amount):
    tax = amount * 0.1
    return tax

# print(calculate_tax(200))



def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    
# generate_report(450, 3)



while True:
    stock = get_valid_input()

    if stock == 'quit':
        break

    elif stock is None:
        failed_entries += 1
        continue
    
    transaction_history.append(stock)
    inventory = process_delivery(inventory, stock)
    tax_amount = calculate_tax(stock)
    if inventory > 500:
        print("Overstock Alert!")
        break

generate_report(inventory, failed_entries)
print("Transaction History:", transaction_history)

