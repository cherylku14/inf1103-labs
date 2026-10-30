import json
from product import Product
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"]
            )
            inventory.add_product(product)
        print("Inventory loaded successfully!")

    except FileNotFoundError:
        print("Inventory file not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        print("Invalid JSON file, Starting with empty inventory.")

    return inventory

def save_inventory(inventory):
    data = []

    for product in inventory.get_all_product():
        data.append(product.to_dict())

    try:
        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Inventory saved successfully!")

    except OSError:
        print("Error saving inventory.") 

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = load_inventory()

while True:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()

    elif option == "2":
        print("Add new Product")

        product_id = input("Product ID: ")
        name = input("Product Name: ")
        price =  float(input("Price: "))
        stock = int(input("Stock quantity: "))

        new_product = Product(product_id, name, price, stock)
        inventory.add_product(new_product)

    elif option == "3":
        print("Update Stock")

        product_id = input("Enter product Id: ")
        product = inventory.search_product(product_id)

        if product is not None:
            print("Product Found:")
            product.display_information()

            new_stock = int(input("New Stock Quantity: "))
            product.update_stock(new_stock)

            print("Stock updated successfully!")

        else:
            print("Product not found.")

    elif option == "4":
        print("Search Product")

        product_id =  input("Enter Product ID: ")
        product = inventory.search_product(product_id)

        if product is not None:
            print("Product Found")
            product.display_information()
        else:
            print("Product not found.")

    elif option == "5":
        print("Saving inventory...")
        save_inventory(inventory)

    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break

    else:
        print("Invalid option. Please try again.")
# inventory = load_inventory()
# inventory.display_all()
# save_inventory(inventory)