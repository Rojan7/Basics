from tic_tac_toe import HumanPlayer,RandomComputerPlayer
import time
class Tic_tac_toe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #list of 9 spaces
        self.winner = None
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    @staticmethod
    def print_board_nums():
     number_board = [[str(i) for i in range (j*3,(j+1)*3)] for j in range(3)]
     for row in number_board:
       print('| ' + ' | '.join(row) + ' |')
    def available_moves(self):
     moves = []
     for (i,spot) in enumerate(self.board):
        if spot == ' ':
            moves.append(i)
     return moves
    def empty_squares(self):
        return ' ' in self.board 
    def num_empty_squares(self):
        return self.board.count(' ')
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.winner = letter
            return True
        return False
    def check_winner(self, square, letter):
        #winner must be checked at rows columns and diagonal
        row_ind = square // 3 # this gives row number
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        #checking the diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


            

def play (game,x_player,o_player,printgame= True):
    if printgame:
        game.print_board_nums()
    letter = 'X'#starts with it

    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
            
        else:
            square = x_player.get_move(game)
            
        if game.make_move(square, letter):
            if printgame:
                print (letter+f' makes a move to square {square}')
                game.print_board()
                print('')
            if game.winner:
                if printgame:
                    print(letter + ' wins!')
                return letter 
            letter = 'O' if letter == 'X' else 'X'
        time.sleep(0.8)
    if printgame:
            print('It\'s a tie!') 
if __name__ == '__main__': #this means if this file is run directly
        x_player = HumanPlayer('X')
        o_player = RandomComputerPlayer('O')
        t = Tic_tac_toe()
        play(t,x_player,o_player,printgame=True) 
        
                


  

 
        
