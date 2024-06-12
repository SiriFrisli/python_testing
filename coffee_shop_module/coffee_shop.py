"""
Testing the coffee shop exercise from the Runestone Academy
"""

# Setting the name for the variables to be used
shop_name = "Siri's Coffee Shop"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]

def order_coffee(size, roast):
    """
    Take an order fom a user
    :param size: a strong containing one of the coffee_sizes
    :param roast: a string containing one of the coffee_roasts
    :return: a message about the coffee order
    """
    return "Here's your {} coffee roasted {}".format(size, roast)

def add_milk_please(fat_content):
    """
    Pretend like we're adding some milk to a coffee
    :param fat_content: a string or integer containing the milkfat content
    :return: a message about having added the milk
    """
    return "I've added the {}% milk".format(fat_content)

def give_tip(tip_amount):
    """
    Take a tip from the user
    :param tip_amount: the tip amount
    :return: nothing
    """
    print("Thank you so much!")
