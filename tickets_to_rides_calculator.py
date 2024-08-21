'''
Whats a AND ,OR and NOT
a is true and b is false =  false
a and b are true = true
a or b are true = true
a or b are false = true
a is false , b is false then a or b is = false
a is true , b is true then a or b is true
a is true , not a means a is false
a is false , not  a means a is true
'''


# Welcome message for the rides
print("Welcome to our Wondering Land of Rides")

# Asking the user for their height in centimeters
height_of_person = int(input("How tall are you in centimeters?\n"))

# Check if the person's height is 150 cm or taller
if height_of_person >= 150:
    # If the height condition is met, ask for the person's age
    age_of_the_person = int(input("How old are you?\n"))

    # Initialize the bill
    bill = 0

    # Nested if-else structure based on age
    # Checking if the person's age is less than 14 or greater than 65
    if 14 > age_of_the_person or age_of_the_person >=70:
        print("No entry")  # If the person is too young or too old, they can't enter
    elif age_of_the_person > 18 and age_of_the_person < 65:
        bill = 10
    elif age_of_the_person > 65 and age_of_the_person <70:
        print("Celebrate and enjoy this day , the  free of cost ")
    else:
        bill = 5

    # Ask if the user wants a photo
    photo = input("Enter y for yes and n for no if you want a photo: ")
    if photo == "y":
        bill += 3

    # Display the final bill
    print(f"Your bill is ${bill}")

else:
    # If the person is shorter than 150 cm, they can't enter
    print("Sorry! Not this time.")
