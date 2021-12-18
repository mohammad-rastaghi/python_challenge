import random
import time


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too High [H], too Low [L], or Correct [C]??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'\nWooow, the computer guessed your number {guess} correctly!!!')
    time.sleep(5)


while True:
    p = input('\nEnter a key for play, or "q" for quit!  ')
    if p == 'q':
        print('\n\nGood luck ...')
        time.sleep(3)
        break
    x = int(input('In which range you want to guess?!  '))
    computer_guess(x)

