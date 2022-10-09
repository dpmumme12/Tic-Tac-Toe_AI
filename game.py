import numpy as np
from player import HumanPlayer, SmartComputerPlayer


class TicTacToe:
    """
    Class for the Tic-Tac-Toe game. It is used to keep track of the board
    and make any moves that could go on the board. Also keeps track if the
    game is over and who the winner is.
    """

    def __init__(self) -> None:
        self.board = np.full((3, 3), ' ')
        self.moves = self.intialize_moves()
        self.GameOver = False
        self.winner = None

    def print_board(self) -> None:
        """Prints the board in it's current state."""

        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums() -> None:
        """Prints the board with the number that correlates to each square."""

        board_nums = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]], dtype='str')
        for row in board_nums:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self) -> list:
        """Returns a list of all available moves that can be played."""

        valid_moves = np.argwhere(self.board == ' ')
        valid_moves = valid_moves.tolist()
        return [key for key, value in self.moves.items() if value.tolist() in valid_moves]

    def intialize_moves(self) -> dict:
        """Function that runs when the class is intialized and
                sets all of the moves that can be made."""

        indices = np.argwhere(self.board == ' ')
        moves = dict()
        for i, index in enumerate(indices):
            moves.update({i: index})
        return moves

    def move(self, move: int, letter: str) -> bool:
        """
        Takes a move and letter as input and tries to make the move on the
        board. ex: move(1, 'X')
        """

        valid_moves = self.available_moves()

        if move not in valid_moves:
            return False

        self.board[tuple(self.moves[move])] = letter

        if self.check_winner(move, letter):
            self.winner = letter
            self.GameOver = True

        if len(valid_moves) == 1:
            self.GameOver = True

        return True

    def check_winner(self, move: int, letter: str) -> bool:
        """Checks the board and see's if the game is over."""

        row_winner = np.all(self.board == letter, axis=1)
        col_winner = np.all(self.board == letter, axis=0)

        if (True in row_winner) or (True in col_winner):
            return True

        if move in (0, 2, 4, 6, 8):
            diag1 = np.diag(self.board)
            diag2 = np.diag(np.fliplr(self.board))

            diag1_winner = np.all(diag1 == letter)
            diag2_winner = np.all(diag2 == letter)

            if diag1_winner or diag2_winner:
                return True

        return False


def play_game(game: TicTacToe, player_1: object, player_2: object) -> None:
    """Funtion to call to play the game."""

    current_move = player_1
    next_move = player_2

    print('#########################################\n'
          '############## Tic-Tac-Toe ##############\n' +
          '#########################################\n')
    print('Here are the moves that correlate to each square')
    game.print_board_nums()
    print()
    input('Press enter to start game!')

    while not game.GameOver:
        if current_move == player_1:
            game.print_board()
            print()
        current_move.make_move(game)

        temp = current_move
        current_move = next_move
        next_move = temp

    if game.winner is None:
        print('It\'s a Tie!')

    else:
        print(f'\n######  {game.winner} wins!!!  ######\n')
    game.print_board()


if __name__ == '__main__':
    play_game(TicTacToe(), HumanPlayer('X'), SmartComputerPlayer('O'))


# ######Function to simulate games between different computer players########
# def game_sim(game, player_1, player_2):
#     current_move = player_1
#     next_move = player_2

#     tie = 0
#     player1_wins = 0
#     player2_wins = 0

#     for i in range(10):
#         while not game.GameOver:
#             current_move.make_move(game)

#             temp = current_move
#             current_move = next_move
#             next_move = temp

#         if game.winner == None:
#             tie += 1

#         else:
#             if game.winner == player_1.letter:
#                 player1_wins += 1
#             else:
#                 player2_wins += 1

#         game.winner = None
#         game.GameOver = False
#         game.board = np.full((3,3), ' ')
#         current_move = player_1
#         next_move = player_2


#     print(f'Ties: {tie}')
#     print(f'Player 1 wins: {player1_wins}')
#     print(f'Player 2 wins: {player2_wins}')


# game_sim(TicTacToe(), SmartComputerPlayer('X'), SmartComputerPlayer('O'))
