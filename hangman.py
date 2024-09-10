import random
from hangman_words import word_list, stages, logo

# TODO -1 Initialize the number of lives
lives = 6

# TODO -2 Display the hangman game logo
print(logo)

# TODO -3 Randomly choose a word from the word list
random_word = random.choice(word_list).lower()

# TODO -4 Create a placeholder string with blanks for each letter in the word
placeholder = ""
word_length = len(random_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO -5 Initialize variables for game status and correct guesses
Game_Over = False
correct_letter = []

# Main game loop: keep running the game until it's over
while not Game_Over:
    # TODO -6 Display the current number of lives left
    print(f"***************** {lives}/6 LIVES LEFT *****************")

    # TODO -7 Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # TODO -8 Initialize display variable to build the current word state
    display = ""

    # TODO -9 Loop through the word and update the display with guessed letters
    for letter in random_word:
        if letter == guess:
            display += letter
            # Add correctly guessed letters to the correct_letter list
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    # TODO -10 Check if the player already guessed the letter
    if guess in correct_letter:
        print("You already guessed it")

    # TODO -11 Deduct a life if the guessed letter is not in the word
    if guess not in random_word:
        print(f"##### Your guess '{guess}' is not in the word! YOU LOSE A LIFE #####")
        lives -= 1

        # TODO -12 If lives reach 0, end the game with a loss
        if lives == 0:
            Game_Over = True
            print(f"***************** The word was {random_word}, YOU LOSE *****************")

    # TODO -13 Print the current state of the word
    print(display)

    # TODO -14 Check if the player has guessed all letters and won the game
    if "_" not in display:
        Game_Over = True
        print("***************** WHAT A BRAIN, YOU WIN *****************")

    # TODO -15 Display the current hangman stage based on remaining lives
    print(stages[lives])

