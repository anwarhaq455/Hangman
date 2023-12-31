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