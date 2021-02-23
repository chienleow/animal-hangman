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
    user_letter = input('Enter a letter:').upper()

user_input = input('Enter a letter:')
print(user_input)



