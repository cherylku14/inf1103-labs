import json
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
# from product import Product
from inventory import Inventory

def load_inventory():
    inventory = Inventory()

    try:
        with open("inventory.json", "r") as file:
            data = json.load(file)

        for item in data:
            if item["type"] == "physical":
                product = PhysicalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["weight"]
                )

            elif item["type"] == "digital":
                product = DigitalProduct(
                    item["product_id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    item["download_size"]
                )

            else:
                print("Unknown product type.")
                continue

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

        if inventory.search_product(product_id) is not None:
            print("Product ID already exists!")

        else: 
            name = input("Product Name: ")

            try:
                price =  float(input("Price: "))
                stock = int(input("Stock quantity: "))

                if price <0 or stock < 0:
                    print("Price and stock cannot be negative.")

                else:
                    print("1. Physical Product")
                    print("2. Digital Product")

                    product_type = input("Select product type: ")

                    if product_type == "1":
                        weight = float(input("Weight(kg): "))

                        if weight < 0:
                            print("Weight cannot be negative.")
                        else:
                            new_stock = PhysicalProduct(
                                product_id, name, price, stock, weight
                            )
                            inventory.add_product(new_stock)

                    elif product_type == "2":
                        download_size = float(input("Download Size(MB): "))

                        if download_size < 0:
                            print("Download size cannotbe negative")
                        else:
                            new_product =  DigitalProduct(
                                product_id, name, price, stock, download_size
                            )
                            inventory.add_product(new_product)

                    else:
                        print("Invalid product type.")

                    # new_product = Product(product_id, name, price, stock)
                    # inventory.add_product(new_product)

            except ValueError:
                print("Invalid input. Price and stock must be numbers.")

    elif option == "3":
        print("Update Stock")

        product_id = input("Enter product Id: ")
        product = inventory.search_product(product_id)

        if product is not None:
            print("Product Found:")
            product.display_information()

            try:
                new_stock = int(input("New Stock Quantity: "))

                if new_stock < 0:
                    print("Stock cannot be negative.")

                else:
                    product.update_stock(new_stock)
                    print("Stock updated successfully!")
            
            except ValueError:
                print("Invalid input. Stock must be a number.")

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