# Welcome message
print("Welcome to our tip calculator!")

# Input from user
bill = float(input("What was your total amount?\n"))
tip_percentage = float(input("What percentage tip would you like to give? (e.g., 10, 20, 30)\n"))
no_of_people = int(input("How many people are there?\n"))

# Calculate the total bill amount including tip
tip_amount = (tip_percentage / 100) * bill
print(f"The tip is: ${round(tip_amount, 2)}.")
bill_with_tip = bill + tip_amount

# Print the total bill amount with tip
print(f"Total bill amount including tip: ${round(bill_with_tip, 2)}")

# Calculate amount per person
amount_per_person = bill_with_tip / no_of_people

# Print the amount each person should pay
print(f"Each person should pay: ${round(amount_per_person, 2)}\n")

# Print the rounded amount
approximate = round(amount_per_person)
print(f"After rounding, each person should pay approximately: ${approximate}")

# Additional example calculations for clarification
print("\nAdditional example calculations for clarification:")

# Calculating percentage and total bill for a fixed example
percentage = 24 / 100
value = 200 * percentage
print(f"24% of 200 is: ${round(value, 2)}")

total_bill = 200 + value
print(f"Total amount for a bill of 200 with 24% tip: ${round(total_bill, 2)}")

# Total amount for 4 people sharing the bill
amount_per_person_example = total_bill / 4
print(f"Each person should pay (for a fixed example): ${round(amount_per_person_example, 2)}")
