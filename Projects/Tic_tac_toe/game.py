class Tic_tac_toe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.winner = None
    def print_board(self):
        for row in [self.board[i*3,(i+1)*3] for i in range(3)]:
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
                


  

 
        
