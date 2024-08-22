import random

# List of names
who_is_rich = ["Esther", "Annies", "Ebinezer", "Rosey", "Peter"]

# Method 1: Randomly select an item using random.choice
rich = random.choice(who_is_rich)
print(rich)  # Output will be a randomly selected name from the list

# Method 2: Randomly select an item using a random index
random_index = random.randint(0, 4)  # Generate a random index between 0 and 4
print(who_is_rich[random_index])  # Output will be the name at the randomly generated index
