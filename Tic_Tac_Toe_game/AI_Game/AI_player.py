import math
import random


class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter

    def get_move(self, game):
        pass
    

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.Input move (0-8): ')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True    # if these are successful, then yay!
            except ValueError:
                print('Invalid square! try again...')
        
        return val
    

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())      # randomly choose one
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square     # return the machine's decision

    def minimax(self, state, player):
        max_player = self.letter        # you want to maximize your score.(in this case, you are computer!)
        other_player = 'X' if player == 'O' else 'O'

        # first, we want to check if the previous move is a winner
        # this is our base case
        if state.current_winner == other_player:
            # we should return the position AND score because we need to track of the score
            # for minimax to work
            return {'position':None,   # position is None because we didn't move anywhere
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else 
                    -1 * (state.num_empty_squares() + 1)}

        elif not state.empty_squares():          # no empty squares, nobody is wons!
            # in tie situation, the utility score is zero.
            return {'position':None, 'score':0}
        
        if player == max_player:
            # because we want to win, our score in each level should be maximize.in each iterate,
            # we try to increment this score
            best = {'position':None, 'score': -math.inf}        # each score should be larger
        else:
            best = {'position':None, 'score': math.inf}         # each score should be smaller
        
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot.
            state.make_move(possible_move, player)

            # step 2: recurse a minimax to simulate a game after making that move
            sim_score = self.minimax(state, other_player)       # now, we alternate players

            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move       # otherwise this will get messed up from the recursion
            
            # step 4: update the dictionaries if necessary
            if player == max_player:
                # successfully maximized the score
                if sim_score['score'] > best['score']:
                    best = sim_score        # replace best
            else:
                # successfully minimized the score
                if sim_score['score'] < best['score']:
                    best = sim_score

        # "best" dictionary contains the best next possible move and the best score that can be araise from it
        return best
