import random
from animals import animals
import string

def get_animal(animals):
    animal = random.choice(animals)
    return animal.upper()

def hangman():
    animal = get_animal(animals)
    word_letters = set(animal)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # getting user input
    while len(word_letters) > 0:
        user_letter = input('Enter a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You have already used that character, please try again.')
        else:
            print('Invalid character, please try again.')

user_input = input('Enter a letter:')
print(user_input)



