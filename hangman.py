import random
from animals import animals
import string

def get_animal(animals):
    animal = random.choice(animals)
    # while ' ' in animal:
    #     animal = random.choice(animals)
    return animal.upper()

def hangman():
    animal = get_animal(animals)
    word_letters = set(animal)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    print("Let's play Hangman!")

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('\nYou have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        # what the current word is (eg. C - T)
        word_list = [letter if letter in used_letters else '-' for letter in animal]
        print(display_hangman(lives))
        print('\nCurrent word: ', ' '.join(word_list))
        
        user_letter = input('\nEnter a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that letter, guess another letter.')
        else:
            print('\nInvalid character, please try again.')
    if lives == 0:
        print('\nYou died, sorry. The animal was', animal)
    else:
        print('\nCongratulations! You have guessed the animal', animal, '!!')

def display_hangman(lives):
    stages = [
            """
                ---------
                |       |
                |       O
                |      \|/
                |       |
                |      / \
                ---
            """,

            """
                ---------
                |       |
                |       O
                |      \|/
                |       |
                |      / 
                ---
            """,

            """
                ---------
                |       |
                |       O
                |      \|/
                |       |
                |      
                ---
            """,

            """
                ---------
                |       |
                |       O
                |      \|/
                |       
                |      
                ---
            """,

            """
                ---------
                |       |
                |       O
                |       |/
                |       
                |      
                ---
            """,

            """
                ---------
                |       |
                |       O
                |      
                |       
                |      
                ---
            """,

            """
                ---------
                |       |
                |       
                |      
                |       
                |      
                ---
            """
    ]
    return stages[lives]

if __name__ == '__main__':
    hangman()



