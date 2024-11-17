# Write a txt file which has a word in each line like:
# Hands
# Legs
# India
# Crow
# Rain
# ...

# Write a python code to read the file and store the words in the list

# Write a function to guess a word randomly from the list.

# Now, write a function which asks user to guess the chosen word letter by letter.
# Show "incorrect" message to the wrong guessed letter. 
# Display  letters in the clue word that were guessed correctly. 

# Let say word is EVAPORATE

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# You left with 5 chances to guess.

# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on.


# 1)Only let the user guess 6 times, and tell the user how many guesses they have left.
# Keep track of the letters the user guessed.
# 2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
# 3)When the player wins or loses, let them start a new game.


import random

def load_words(file_path):
    """Loads words from the input file."""
    word_list = []
    with open(file_path, 'r') as file:
        for line in file:
            word_list.append(line.strip().lower())
    return word_list


def random_guess(word_list):
    """Selects a random word from the word list."""
    guessed_word = random.choice(word_list)
    return guessed_word


def display_word_progress(random_word, correct_guess_set):
    """Displays the current progress of the word with guessed letters."""
    display = ''.join([letter if letter in correct_guess_set else '_' for letter in random_word])
    return display


def user_guess(word_list):
    """Main game logic for Hangman."""
    random_word = random_guess(word_list)
    correct_guess_set = set()
    guessed_letters = set()
    guess_count = 6

    print("Welcome to Hangman!")
    print("Your word to guess has been chosen.")
    print("You have 6 attempts to guess it!")

    while guess_count > 0:
        print(f"Word: {display_word_progress(random_word, correct_guess_set)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Remaining Attempts: {guess_count}")
        letter = input("Guess your Letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please guess a single valid letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(letter)

        if letter in random_word:
            correct_guess_set.add(letter)
            print("Correct guess!")
            if all(letter in correct_guess_set for letter in random_word):
                print(f"Congratulations! You guessed the word: {random_word}")
                return
        else:
            guess_count -= 1
            print("Incorrect guess!")

    print(f"Out of attempts! The word was: {random_word}")


if __name__ == "__main__":
    file_path = 'C:/Users/nisha/Desktop/paceWisdom2/pythonDS/Hangman_8.2/input.txt'
    word_list = load_words(file_path)
    while True:
        user_guess(word_list)
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != 'yes':
            print("Thanks for playing Hangman!")
            break
