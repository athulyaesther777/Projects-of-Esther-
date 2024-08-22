import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
print(" Welcome to Rock , Paper or Scissors ")
user = input("Do you wanna play with me? yes or no\n").lower()


if user == "yes":
    print("Thank you,Let\'s play then....")
else:
    print("My bad")
    exit()

choices =[rock , paper,scissors]
user_input = int(input(" Which one you choose Rock (0) ,"
                       " Paper (1) or Scissors (2)\n"))
if user_input ==0:
    user_choice = rock
elif user_input ==1:
    user_choice = paper
elif user_input:
    user_choice = scissors
else:
    print("Invalid input")
    exit()
print(f"You choice :\n{user_choice}")

computer_input = random.randint(0,2)
computer_choices = choices[computer_input]
print(f" Computer chose :\n {computer_choices}")

if user_input == computer_input:
    print("Draw match  ")
elif (user_input == 0 and computer_input == 1) or \
    (user_input == 0 and computer_input == 1) or \
    (user_input == 0 and computer_input == 1):
    print("You win!")
else:
    print("You lose")

