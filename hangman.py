import random
from animals import animals

def get_animal(animals):
    animal = random.choice(animals)
    return animal.upper()

def hangman():
    animal = get_animal(animals)
    word_letters = set(animal)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 5

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters:')

