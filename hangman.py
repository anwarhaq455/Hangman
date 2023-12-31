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


# milestone_4.py

# Step 1
class Hangman:
    # Step 2
    def __init__(self, word_list, num_lives=5):
        # Step 3
        self.word = random.choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

# Task 2: Create methods for running the checks
# Step 1 (in milestone_4.py)
    def check_guess(self, guess):
        # Step 2
        guess = guess.lower()

        # Step 3 (continued)
        if guess.isalpha() and len(guess) == 1:
            # Step 4 (continued in milestone_4.py)
            if guess in self.word:
                # Step 3 (continued)
                print(f"Good guess! {guess} is in the word.")
                for i, letter in enumerate(self.word):
                    if letter == guess:
                        self.word_guessed[i] = guess
                        self.num_letters -= 1
            else:
                # Step 4 (continued)
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")

# Step 2 (continued)
    def ask_for_input(self):
        # Step 1
        while True:
            # Step 2
            guess = input("Guess a letter: ")

            # Step 3
            if guess.isalpha() and len(guess) == 1:
                # Step 4
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
            else:
                # Step 5
                print("Invalid letter. Please, enter a single alphabetical character.")

# milestone_4.py

# Task 3 (in check_guess method, after Step 3)
            self.num_letters -= 1
            for i, letter in enumerate(self.word):
                if letter == guess:
                   self.word_guessed[i] = guess



# milestone_4.py

# Task 4 (in check_guess method, after Step 3)
            else:
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")


# milestone_5.py

# Step 1
def play_game(word_list):
    # Step 2
    num_lives = 5
    game = Hangman(word_list, num_lives)

    # Step 3
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

# Step 2
play_game(word_list)

#DESCREPTION:
#In this game there is 5 fruit name when run the programe computer pick one fruit from the 5 fruit in the list each time and ask you to guess the fruit letter
#and if you Guess corettly give you message its correct other wise ask you try again and give you five live to guess if you are wrong if you guess right you won other wise give you message you lost


 
