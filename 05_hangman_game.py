import random
import string
from words import words
import time


def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman(num):
    lives = num
    word = get_valid_word(words)  # letters in the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)   # the letters in the English dictionary
    used_letters = set()  # what the user has guessed

    while len(word_letters) > 0 and lives > 0:
        # letters used
        print(f'\nYou have {lives} lives and you have used these letters: ', ' '.join(used_letters))

        # what the current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        # getting a letter from user
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print('the letter was not in word.')
                lives -= 1

        elif user_letter in used_letters:
            print('You have already used that letter! please Try again...  \n')

        else:
            print('Invalid Character!! please Try again... \n')
    if lives == 0:
        print(f'Sorry! <<< You Died >>>  the word was "{word}"')
        time.sleep(4)
        return
    else:
        print(f'\n\nCongratulations!! the current word was :  {word}')
        time.sleep(4)

hangman(10)
