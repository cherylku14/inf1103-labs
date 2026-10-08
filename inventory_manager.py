import json

"""
inventory = [
    {
        "id": "P001",
        "name": "Laptop",
        "price": 1200.00,
        "stock": 15
    },
    {
        "id": "P002",
        "name": "Mouse",
        "price": 25.50,
        "stock": 40
    },
    {
        "id": "P003",
        "name": "Keyboard",
        "price": 45.00,
        "stock": 25
    }
]
"""

def load_inventory():
    try:
        file = open("inventory.json", "r")
        inventory = json.load(file)
        file.close()
        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory

    except FileNotFoundError:
        print("inventory.json not found")
        return []


def display_all(inventory):
    print("Current Inventory")
    print("------------------------------------------------")

    for product in inventory:
        print("ID:", product["id"],
        " | Name:", product["name"],
        " | Price: $" + format(product["price"], ".2f"),
        " | Stock:", product["stock"]
        )

    print("------------------------------------------------")


def add_product(inventory):
    print("Add New Product")

    product_id = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock quantity: "))

    new_product = {
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    inventory.append(new_product)
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print("Name:", product["name"])
            print("Current Stock:", product["stock"])

            new_stock = int(input("New Stock Quantity: "))
            product["stock"] = new_stock

            print("Stock updated successfully!")
            return

    print("Product not found.")


def search_product(inventory):
    print("Search Product")

    product_id = input("Enter Product ID: ")

    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("------------------------------------------------")
            print("ID:", product["id"])
            print("Name:", product["name"])
            print("Price: $" + format(product["price"], ".2f"))
            print("Stock:", product["stock"])
            print("------------------------------------------------")
            return

    print("Product not found.")


def save_inventory(inventory):
    file = open("inventory.json", "w")
    json.dump(inventory, file, indent=4)
    file.close()

    print("Inventory saved successfully to inventory.json.")


print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")

inventory = load_inventory()
print("\n")

print("----------- MENU -----------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit")
print("----------------------------\n")

while True:
    option = input("Enter options: ")

    if option == "1":
        display_all(inventory)
        print("\n")

    elif option == "2":
        add_product(inventory)
        print("\n")

    elif option == "3":
        update_stock(inventory)
        print("\n")

    elif option == "4":
        search_product(inventory)
        print("\n")

    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)
        print("\n")

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option. Please try again.")

# display_all(inventory)
# add_product(inventory)
# display_all(inventory)
# update_stock(inventory)
# display_all(inventory)
# search_product(inventory)
# add_product(inventory)
# save_inventory(inventory)



