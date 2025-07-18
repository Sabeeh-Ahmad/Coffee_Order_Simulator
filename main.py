# ☕️ Coffee Order Simulator - Session 3: Data Types and Operators ☕️
# Welcome to Code Café! Let's take your order using Python.
# This session is all about how we can talk to Python (input) and how it talks back (output).


# Print a welcome message
print("Welcome to Coffee Order Simulator!\n")

# Ask for the customer's name
name = input("Enter your name: ").capitalize()

# Ask for cup size
size = input("Enter the cup size (small/medium/large): ").capitalize()

# Ask for coffee type
coffee_type = input("Enter the coffee type (Espresso, Latte, Capuccino): ").capitalize()

# Ask for extra toppings
toppings = input("Enter the extra toppings (e.g. None, Whipped Cream, Nutella, Mint): ").capitalize()
# Ask for takeaway or dine-in
order_type = input("Takeaway or Dine-in?: ").capitalize()

# Print a cute little receipt
print("\n")
print("-" * 30)

print("Customer: ", name)

print("Coffee size: ", size)

print("Coffee type: ", coffee_type)

print("Extra Toppings: ", toppings)

print("Order Type: ", order_type)
# Use sep and end for formatting fun



print("Thank you for ordering from Code Café!")
print("Your coffee will be ready shortly. Enjoy!")
print("-" * 30)

# 💡 Notes for learners:
# - input() lets Python take information from the user.
# - print() displays information back to the user.
# - You can decorate your output using escape characters like \n (new line) and special parameters like end= and sep=
# - datetime module helps you work with real-world time and date
