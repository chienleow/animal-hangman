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
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

user_input = input('Enter a letter:')
print(user_input)



