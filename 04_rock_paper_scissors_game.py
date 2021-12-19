import random
import time


def play():

    user = input('\nwhat is you choice?\n"R" for rock, "P" for paper or "S" for scissors.? ').lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You Won!!'

    return 'You Lost!!'


# r > s, s > p, p > r
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False


while True:
    play_ = input('\nStart playing? press any key...   press "q" for quit!  ').lower()
    if play_ == 'q':
        break
    else:
        print(play())
        time.sleep(3)
