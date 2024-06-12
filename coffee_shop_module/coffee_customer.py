import coffee_shop_module.coffee_shop as coffee_shop

print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)

# Ask for some input from the customer
order_size = input("What size coffee do you wnat?")
order_roast = input("What roast do you want?")

# Send the order to the shop
shop_says = coffee_shop.order_coffee(order_size, order_roast)

# Print out whatever it gave back to us
print(shop_says)

# Check if the customer wants milk
add_milk_response = input("Do you wnat milk (y/n)?")

# Convert response to lowercase, then check for a "yes"
if "y" in add_milk_response.lower():
    milk_fat = input("What percent milk do you want?")
    shop_says = coffee_shop.add_milk_please(milk_fat)
    # Print out answer from shop
    print(shop_says)

tip_amount = input("Tip amount?")
coffee_shop.give_tip(tip_amount)

