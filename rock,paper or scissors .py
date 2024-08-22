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

def print_scoreboard(user_score, computer_score, round_num):
    print(f"\n--- Round {round_num} Scoreboard ---")
    print(f"You: {user_score} | Computer: {computer_score}")
    print(f"----------------------------------")

print("Welcome to Rock, Paper, Scissors!")
print("You will play up to 10 rounds.")

user_total_score = 0
computer_total_score = 0
round_num = 0
max_rounds = 10

while round_num < max_rounds:
    round_num += 1
    print(f"\nRound {round_num}")
    
    user_input = input("Which one do you choose? Rock (0), Paper (1), or Scissors (2)\n")
    
    if user_input not in ['0', '1', '2']:
        print("Invalid input, please enter 0, 1, or 2.")
        round_num -= 1
        continue
    
    user_input = int(user_input)
    
    choices = [rock, paper, scissors]
    user_choice = choices[user_input]
    
    computer_input = random.randint(0, 2)
    computer_choice = choices[computer_input]
    
    print(f"You chose:\n{user_choice}")
    print(f"Computer chose:\n{computer_choice}")
    
    if user_input == computer_input:
        print("Draw match!")
    elif (user_input == 0 and computer_input == 2) or \
         (user_input == 1 and computer_input == 0) or \
         (user_input == 2 and computer_input == 1):
        print("You win this round!")
        user_total_score += 1
    else:
        print("Computer wins this round!")
        computer_total_score += 1
    
    print_scoreboard(user_total_score, computer_total_score, round_num)

print("\nGame Over!")
print("Final Scoreboard:")
print(f"You: {user_total_score} | Computer: {computer_total_score}")

if user_total_score > computer_total_score:
    print("Congratulations! You are the winner!")
elif user_total_score < computer_total_score:
    print("Sorry, Computer wins this time.")
else:
    print("It's a draw!")
