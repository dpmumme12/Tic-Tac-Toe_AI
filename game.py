import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full((3,3), ' ')
        self.moves = self.intialize_moves()

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        board_nums = np.array([[0,1,2],[3,4,5],[6,7,8]], dtype='str')
        for row in board_nums:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = np.argwhere(self.board == ' ')
        return moves

    def intialize_moves(self):
        indices = np.argwhere(self.board == ' ')
        moves = dict()
        for i, index in enumerate(indices):
            moves.update({i: index})

        return moves

    def make_move(self, move, letter = None):
        if not self.moves[move] in self.available_moves():
            pass

        self.board[tuple(self.moves[move])] = 'X'

        if self.check_winner(move, letter):
            pass

    def check_winner(self, move, letter):
        #row, col = self.moves[move]
        
        row_winner = np.all(self.board == letter, axis=1)
        col_winner = np.all(self.board == letter, axis=0)

        if (True in row_winner) or (True in col_winner):
            return True

        if move in (0,2,4,6,8):
            diag1 = np.diag(self.board)
            diag2 = np.diag(np.fliplr(self.board))

            diag1_winner = np.all(diag1 == letter)
            diag2_winner = np.all(diag2 == letter)

            if diag1_winner or diag2_winner:
                return True
        
        return False
  

game = TicTacToe()

game.make_move(4)


