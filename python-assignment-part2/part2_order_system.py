menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

print("Task 1 — Explore the Menu ")

all_cat = []

for item_details in menu.values(): # loop to store all the unique categories from the menu first
    cat= item_details["category"]
    if cat not in all_cat:
        all_cat.append(cat)

for category in all_cat:
    print("\n===== " + category + " =====")

    for item_name in menu:
        item_info= menu[item_name]
        if item_info["category"] == category:
            price = item_info["price"]

            if item_info["available"] == True:
                status = "[Available]"
            else:                
                status = "[Unavailable]"

            print(" " + item_name + " - ₹" + str(price) + " " + status)


print("\n  Menu Stats")

tot_items = len(menu)    # to count the total number of items in the menu
print(f"Total Menu Items: {tot_items}")

count = 0             # to count the number of available items in the menu
for item_name in menu:
    if menu[item_name]["available"] == True:
        count += 1

print(f"Available Items: {count}")

all_item_names = list(menu.keys()) # to store all the item names in a list
most_expensive = all_item_names[0] 
for item_name in menu:
    if menu[item_name]["price"] > menu[most_expensive]["price"]:  # to find the most expensive item in the menu by comparing the price of each item with the current most expensive item found
        most_expensive = item_name

most_expensive_price = menu[most_expensive]["price"]
print(f"Most Expensive Item: {most_expensive} - ₹{most_expensive_price}")


print("\n Items priced under ₹150:")
for item_name in menu:   # loop to find and print all the items in the menu that are priced under ₹150
    if menu[item_name]["price"] < 150:
        print(f" - {item_name}: ₹{menu[item_name]['price']}")

print("\nTask 2 — Cart Operations")
cart=[]

def add_to_cart(item_name,qty):  #function to add items to the cart by taking the items name and quantity as input and checking the availability

    if item_name not in menu:
        print(f"Sorry, {item_name} is not on the menu.")
        return
    
    if menu[item_name]["available"] == False:
        print(f"Sorry, {item_name} is currently unavailable.")
        return
    
    for entry in cart:  # loop to check if the item is already in the cart and if it is then update the quantity and total price for that item in the cart
        if entry["item"] == item_name:
            entry["quantity"] += qty
            print(f" {item_name} was already in cart. Quantity updated to {entry['quantity']}")
            return
    
    new_entry = {}
    new_entry["item"] = item_name
    new_entry["quantity"] = qty
    new_entry["price"] = menu[item_name]["price"]
    
    cart.append(new_entry)
    print(f" {item_name} added to the cart. Quantity: {qty}")


def remove_from_cart(item_name):  # function to remove an item from the cart by taking the item name as input and checking if it is in the cart or not
    for entry in cart:
        if entry["item"] == item_name:
            cart.remove(entry)
            print(f" {item_name} removed from the cart.")
            return
    
    print(f" {item_name} is not in the cart.")

def update_qty(item_name, new_qty):  # function to update the quantity of an item in the cart by taking the item name and new quantity as input and checking if the item is in the cart or not
    for entry in cart:
        if entry["item"] == item_name:
            entry["quantity"] = new_qty
            print(f" Quantity of {item_name} updated to {new_qty}")
            return
    
    print(f" {item_name} is not in the cart.")

def view_cart():  # function to view the current items in the cart along with their quantity and total price for each item and the overall total price of the cart
    if len(cart) == 0:
        print(" Your cart is empty.")
        return
    else:
        print("\nCurrent Cart:")
        
        for entry in cart:
            print(f" - {entry['item']}: Quantity: {entry['quantity']}, at: ₹{entry['price']}")
    
# Simuulating order sequence as per instructions   
add_to_cart("Paneer Tikka", 2)   
view_cart()

add_to_cart("Gulab Jamun", 1)
view_cart()

add_to_cart("Paneer Tikka", 1)
view_cart()

add_to_cart("Mystery Burger", 1)
view_cart()

add_to_cart("Chicken Wings", 1)
view_cart()

remove_from_cart("Gulab Jamun")
view_cart()

print("\n======== Order Summary ========")

subtotal = 0

for entry in cart:
    item_total = entry["quantity"] * entry["price"]
    subtotal += item_total
    print(f"{entry['item']} x {entry['quantity']} @ ₹{entry['price']} each: ₹{item_total}")

print("-----------------------------")

gst_amt = subtotal * 0.05
total_payable = subtotal + gst_amt

print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (5%): ₹{gst_amt:.2f}")
print(f"Total Payable: ₹{total_payable:.2f}")
print("===============================")


print("\n Task 3 — Inventory Tracker with Deep Copy")

import copy

inventory_backup = copy.deepcopy(inventory)  # creating a deep copy of the inventory dictionary to make changes without affecting the original inventory

inventory["Ice Cream"]["stock"] = 25

print(f"\n inventory Ice Cream: {inventory['Ice Cream']['stock']} units")
print(f" inventory_backup Ice Cream stock : {inventory_backup['Ice Cream']['stock']} units")
print(" The backup was not affected. Deep copy is working correctly")

inventory["Ice Cream"]["stock"] = 7

print(f"\n --Deducting stock based on the final cart --")

for entry in cart:
    item_name = entry["item"]
    quant = entry["quantity"]
    current_stock = inventory[item_name]["stock"]
    
    if current_stock < quant:
        print(f" Warning!!!! Not enough stock for {item_name}. Available: {current_stock}, Required: {quant}. Deducting only available stock.")
        inventory[item_name]["stock"] = 0
    else:
        inventory[item_name]["stock"] -= quant
    print(f" Deducted: {quant} units. Remaining stock for {item_name}: {inventory[item_name]['stock']} units")


print(f"\n -- Reorder Alerts --")

trigger = False
for item_name in inventory:
    current_stock = inventory[item_name]["stock"]
    reorder_level = inventory[item_name]["reorder_level"]
    
    if current_stock <= reorder_level:
        print(f" Reorder Alert: {item_name} - Only {current_stock} units left, Reorder Level: {reorder_level}.")
        trigger = True

if trigger == False:
    print(f" All items have sufficient stock. No reorder needed.")


print(f"\n -- Inventory vs Backup --")
print(f" Item Name         |  Current Stock | Backup Stock")

for item_name in inventory:
    current = inventory[item_name]["stock"]
    backup = inventory_backup[item_name]["stock"]
    
    if current != backup:
        note = " (Updated)"
    else:
        note = ""
    
    print(f" {item_name}     |      {current}     |      {backup}     | {note}")


print("\n Task 4 — Daily Sales Log Analysis")

print(f"\n -- Revenue Per Day --")

# Loop to calculate and print the total revenue generated for each day by summing up the total from each order in the sales log for that day

daily_revenue = {}

for date in sales_log:
    total_for_day = 0
    orders_on_that_day = sales_log[date]

    for order in orders_on_that_day:
        total_for_day += order["total"]
    
    daily_revenue[date] = total_for_day
    print(f" {date}: ₹{total_for_day:.2f}")

# to find the best selling day
# starting with the first date as the best selling day and then comparing the revenue of each day with the current best selling day to find the day with the highest revenue

all_dates = list(daily_revenue.keys())
best_selling_day = all_dates[0]

for date in daily_revenue:
    if daily_revenue[date] > daily_revenue[best_selling_day]:
        best_selling_day = date

print(f"\n Best Selling Day: {best_selling_day} with revenue of ₹{daily_revenue[best_selling_day]:.2f}")

# to find the most ordered item
# counting how many times each item appears across all orders in the sales log and then finding the item with the highest count

item_count = {}

for date in sales_log:
    orders_on_that_day = sales_log[date]

    for order in orders_on_that_day:
        items_in_order = order["items"]

        for item in items_in_order:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1
            
all_items = list(item_count.keys())
most_ordered_item = all_items[0]

for item in item_count:
    if item_count[item] > item_count[most_ordered_item]:
        most_ordered_item = item

print(f"\n Most Ordered Item: {most_ordered_item} with {item_count[most_ordered_item]} orders")

# adding a new day to sales_log and reprint stats

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

print(f"\n Updated Revenue Per Day after adding new sales data for 2025-01-05:")

# recalculating daily revenue after adding new sales data for 2025-01-05 and printing the updated revenue for each day
daily_rev_updated = {}

for date in sales_log:
    total_for_day = 0
    orders_on_that_day = sales_log[date]

    for order in orders_on_that_day:
        total_for_day += order["total"]
    
    daily_rev_updated[date] = total_for_day
    print(f" {date}: ₹{total_for_day:.2f}")

# finding the new best selling day after adding new sales data for 2025-01-05 by comparing the revenue of each day with the current best selling day to find the day with the highest revenue
all_dates = list(daily_rev_updated.keys())
best_selling_day_updated = all_dates[0]

for date in daily_rev_updated:
    if daily_rev_updated[date] > daily_rev_updated[best_selling_day_updated]:
        best_selling_day_updated = date

print(f"\n Updated Best Selling Day: {best_selling_day_updated} with revenue of ₹{daily_rev_updated[best_selling_day_updated]:.2f}")

# numbered list of all orders

print(f"\n Numbered List of All Orders:")

order_number = 1

for date, orders in sales_log.items():
    for index, order in enumerate(orders,start=1):
        items_in_order = ", ".join(order["items"])
        print(f" {order_number}. [{date}] Order # {order['order_id']} - Total: ₹{order['total']:.2f} - Items: {items_in_order}")
        order_number += 1