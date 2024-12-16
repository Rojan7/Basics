import random
from words import words
import string

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display_hangman(lives):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """,  # 0 lives left
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,  # 1 life left
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,  # 2 lives left
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,  # 3 lives left
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,  # 4 lives left
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,  # 5 lives left
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """,  # 6 lives left
    ]
    return stages[lives]

def Hangman():
    word = get_valid_words(words)
    word_letters = set(word)  # letters in the word generated
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6

    print("Welcome to Hangman!")
    
    while len(word_letters) > 0 and lives > 0:
        # Display current state of the game
        print(display_hangman(lives))
        print('You have used these letters:', " ".join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word:', " ".join(word_list))
        
        # Get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good guess!")
            else:
                lives -= 1
                print("Wrong guess!")
        elif user_letter in used_letters:
            print("You already guessed that letter!")
        else:
            print("Invalid input. Please guess a valid letter.")
    
    # End of game
    if lives == 0:
        print(display_hangman(lives))
        print(f"You lost! The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word: {word}")

Hangman()
