print("Welcome to our Fried Chicken Exploring Hut \n")

# Define items with their prices
items = [
    ("Small Bucket Fried Chicken", 180),
    ("Medium Bucket Fried Chicken", 200),
    ("Large Bucket Fried Chicken", 240),
    ("Bun (1)", 10),
    ("Dipping", 30)
]

# Print item options and prices
print(f"{'Item':<30} {'Price'}")
for item, value in items:
    print(f"{item:<30} {value}")

# Initialize total price
total_price = 0

# Get user's choice for bucket size
bucket_size = input("\nWhich size would you like to choose? (e.g., S, M, or L) \n").upper()
if bucket_size == "S":
    total_price += 180
    print("Small Bucket Fried Chicken: 180 rupees")
elif bucket_size == "M":
    total_price += 200
    print("Medium Bucket Fried Chicken: 200 rupees")
elif bucket_size == "L":
    total_price += 240
    print("Large Bucket Fried Chicken: 240 rupees")
else:
    print("Can't recognize? Type a valid option.")
    exit()

# Get user's choice for buns
buns = input("Do you prefer buns with the fried chicken? (say: Yes or No) \n").lower()
if buns == "yes":
    no_of_buns = int(input("How many buns do you need? \n"))
    buns_price = no_of_buns * 10
    total_price += buns_price
    print(f"Buns ({no_of_buns}): {buns_price} rupees")
else:
    print("No buns selected.")

# Get user's choice for dipping
dipping = input("Do you need extra dipping? (say: Yes or No) \n").lower()
if dipping == "yes":
    total_price += 30
    print("Extra Dipping: 30 rupees")
else:
    print("No extra dipping.")

# Print total amount with breakdown
print(f"\nBreakdown of total amount:")
print(f"Bucket size: {total_price - (buns_price if buns == 'yes' else 0) - 30} rupees")
if buns == "yes":
    print(f"Buns: {buns_price} rupees")
print(f"Dipping: 30 rupees")

print(f"The total amount is: {total_price} rupees.")
