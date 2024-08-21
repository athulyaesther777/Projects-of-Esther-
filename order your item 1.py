# Print a welcome message
print("Welcome to our Fried Chicken Exploring Hut \n")

# Define a list of items with their prices
items = [
    ("Small Bucket Fried Chicken", 180),  # Tuple for small bucket
    ("Medium Bucket Fried Chicken", 200),  # Tuple for medium bucket
    ("Large Bucket Fried Chicken", 240),   # Tuple for large bucket
    ("Bun (1)", 10),                      # Tuple for one bun
    ("Dipping", 30)                       # Tuple for dipping
]

# Print the header for the items list
print(f"{'Item':<30} {'Value'}")

# Iterate over each tuple in the items list
for item, value in items:
    # Print each item and its price
    print(f"{item:<30} {value}")

"""
Explanation of tuple unpacking:
In the for loop `for item, value in items:`, the loop unpacks each tuple into two variables:
- `item`: The name of the item (e.g., "Small Bucket Fried Chicken").
- `value`: The price of the item (e.g., 180).

Python handles this unpacking automatically because each tuple in the `items` list has exactly two elements.
"""

# Initialize the total price
price = 0

# Get user's choice for bucket size
bucket_size = input("\nWhich size would you like to choose? (e.g., S, M, or L) \n").upper()
if bucket_size == "S":
    # Add price for small bucket
    price += 180
elif bucket_size == "M":
    # Add price for medium bucket
    price += 200
elif bucket_size == "L":
    # Add price for large bucket
    price += 240
else:
    # Handle invalid bucket size
    print("Can't recognize? Type a valid option.")
    exit()

# Get user's choice for buns
buns = input("Do you prefer buns with the fried chicken? (say: Yes or No) \n").lower()
if buns == "yes":
    # Ask for the number of buns
    no_of_buns = int(input("How many buns do you need? \n"))
    # Calculate and add the price for buns
    price += no_of_buns * 10
elif buns == "no":
    print("Okay, no buns then.")
else:
    # Handle invalid input for buns
    print("Invalid input. Please check.")

# Get user's choice for dipping
dipping = input("Do you need extra dipping? (say: Yes or No) \n").lower()
if dipping == "yes":
    # Ask for the number of dips
    no_of_dipping = int(input("How many dips do you need? \n"))
    # Calculate and add the price for dipping
    price += no_of_dipping * 30
else:
    # Handle invalid input for dipping
    print("Invalid input !!!")

# Print the total amount
print(f"The total amount is: {price} rupees.")
