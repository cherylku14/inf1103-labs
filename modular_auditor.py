inventory = 0
failed_entries = 0

# def get_valid_input():
#     while True: 
#         stock = input("Enter a stock quantity (or 'quit)： ")

#         if stock == 'quit':
#             return "quit"

#         elif stock.isdigit():
#             return int(stock)

#         else:
#             print("Invalid input")

# result = get_valid_input()
# print(result)

def process_delivery(current_total, new_value):
    updated_total = new_value + current_total
    return updated_total

delivery = process_delivery(400,150)
print(delivery)


# while True:
#     stock = input("Enter a stock quantity (or 'quit'): ")

#     if stock == "quit":
#         break

#     elif not stock.isdigit():
#         print("Invalid input")
#         failed_entries += 1
#         continue

#     else:
#         stock = int(stock)

#     inventory += stock

#     if inventory > 500:
#         print("Overstock Alert!")
#         break

# print("Total Units Processed:", inventory )
# print("Number of Failed/Rejected Entries:", failed_entries)