import random
import time

start_num = 1
end_num = 100

num = random.randint(start_num, end_num)
guess = None

while guess != num:
    guess = int(input(f'\nGuess a number between {start_num} and {end_num}: '))

    if guess == num:
        print('Congratulation!! You Won!!', f'\n\nYour num was {num}')
        time.sleep(4)
        break
    else:
        if guess < num:
            print('Nope!!! sorry, try again!!\nGo Upper!')
        else:
            print('Nope!!! sorry, try again!!\nGo Lower!')



