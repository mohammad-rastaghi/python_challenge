import time
from AI_player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]        #we will use a single list to rep 3x3 board
        self.current_winner = None      #keep track of winner!

    def print_board(self):
        # this is just getting the rows
        lines = [self.board[0:3], self.board[3:6], self.board[6:]]
        for row in lines:
            print('| ' + ' | '.join(row) + ' |')
        #for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
        #    print('| ' + ' | '.join(row) + ' |')
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1) *3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        #return [i for i,spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'x'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make the move(assign square into letter)
        #then return True.if invalid, return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        # winner if 3 in a row in anywhere.we have to check all of these!
        # first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        #check colomn
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        # (0, 2, 4, 6, 8) these are only posible positions for win diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]   #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]   #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        #if all of these Fail
        return False


def play(game, x_player, o_player, print_game = True):
    #returns the winner of the game(the letter)! or None for a Tie!
    if print_game:
        game.print_board_nums()

    letter = 'X'    #starting letter

    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        #lets define a function to make a move!
        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('')       # just an Empty line

        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter

        #after we made moves, we need to alternate latters!
        #letter = 'O' if letter == 'X' else 'X'
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'

        # tiny break to make things easier to read
        if print_game:
            time.sleep(0.8)

    # what if we can't Won??
    if print_game:
        print('It\'s a tie!')

'''
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game = True)
'''


if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for i in range(1000):
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        game = TicTacToe()
        result = play(game, x_player, o_player, print_game = False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    
    # print the final results
    print(f'After 1000 game, your machine achieve wins: {o_wins}, loses: {x_wins}, ties: {ties}')
