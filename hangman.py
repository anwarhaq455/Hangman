#step 1
favorite_fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Step 2
word_list = favorite_fruits

# Step 3
print(word_list)


# milestone_2.py

# Step 1
import random

# Step 3
word = random.choice(word_list)

# Step 4
print(word)

 #milestone_2.py

# Step 1
guess = input("Enter a single letter: ")

# Step 2
print("Guess:", guess)


if len(guess) ==1 and guess.isalpha():
    #step 2
    print("Good guess!")
else:
    #step 3
    print("Oops! That is not a valid input.")

while True:
    # Step 2
    guess = input("Guess a letter: ")

    # Step 3
    if guess.isalpha() and len(guess) == 1:
        # Step 4
        break
    else:
        # Step 5
        print("Invalid letter. Please, enter a single alphabetical character.")

# milestone_3.py

# Step 3 (after Step 4)
if guess in word:
    # Step 2
    print(f"Good guess! {guess} is in the word.")
else:
    # Step 3
    print(f"Sorry, {guess} is not in the word. Try again.")
    
    
# milestone_3.py

# Step 1
def check_guess(guess):
    # Step 2
    guess = guess.lower()
    # Step 3 (moved from milestone_3.py)
    if guess.isalpha() and len(guess) == 1:
        # Step 4 (continued in milestone_3.py)
        if guess in word:
            # Step 3 (continued)
            print(f"Good guess! {guess} is in the word.")
        else:
            # Step 4 (continued)
            print(f"Sorry, {guess} is not in the word. Try again.")

# Step 2 (in milestone_3.py)
def ask_for_input():
    # Step 1
    while True:
        # Step 2
        guess = input("Guess a letter: ")

        # Step 3
        if guess.isalpha() and len(guess) == 1:
            # Step 4
            check_guess(guess)
            break
        else:
            # Step 5
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 3 (in milestone_3.py)
ask_for_input()
