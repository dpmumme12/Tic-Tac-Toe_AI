import random
import math

"""
This module consatins all of the different player classes
that can be used in the Tic-Tac-Toe game.
"""


class HumanPlayer:
    """
    Class that represent s a Human playe for Tic-Tac-Toe. If this
    class is used the player will be required to input each move
    through the command line.
    """

    def __init__(self, letter: str) -> None:
        self.letter = letter

    def make_move(self, game) -> None:
        valid_move = False
        while not valid_move:
            move = input(self.letter + '\'s turn, Input move (0-8): ')
            try:
                valid_move = game.move(int(move), self.letter)
            except Exception:
                pass


class ComputerPlayer:
    """
    Class that represents a computer player for Tic-Tac-Toe. If this class
    is used it will randomly select a move from the list of available moves.
    """

    def __init__(self, letter: str) -> None:
        self.letter = letter

    def make_move(self, game) -> None:
        moves = game.available_moves()
        move = random.choice(moves)
        game.move(move, self.letter)


class SmartComputerPlayer:
    """Class that represents a A.I. player for Tic-Tac-Toe. If this class
        is used it will use an algorithm to find the best move to play."""

    def __init__(self, letter: str) -> None:
        self.letter = letter

    def make_move(self, game) -> None:
        if len(game.available_moves()) == 9:
            move = random.choice([0, 2, 6, 8])
            game.move(move, self.letter)

        else:
            other_player = 'O' if self.letter == 'X' else 'X'
            move = self.minimax(other_player, game, True)['move']

            game.move(move, self.letter)

    def minimax(self, other_player: str, game: object, MaximizingPlayer: bool) -> dict[str, int]:
        """
        The algorithm that runs to find the best possible move to make.
        It use's the MiniMax algorithm which utilizes depth first search
        to play every possible move and return the move that is best.
        """

        if game.GameOver:
            moves_left = len(game.available_moves())
            if game.winner is None and moves_left == 0:
                return {'score': 0}

            elif game.winner == self.letter:
                return {'score': moves_left + 1}

            elif game.winner == other_player:
                return {'score': (moves_left + 1) * -1}

        if MaximizingPlayer:
            max_eval = {'move': None, 'score': -math.inf}
            valid_moves = game.available_moves()
            for move in valid_moves:
                game.move(move, self.letter)
                sim_eval = self.minimax(other_player, game, False)

                game.board[tuple(game.moves[move])] = ' '
                game.winner = None
                game.GameOver = False

                if sim_eval['score'] > max_eval['score']:
                    max_eval['score'] = sim_eval['score']
                    max_eval['move'] = move
            return max_eval

        else:
            min_eval = {'move': None, 'score': math.inf}
            valid_moves = game.available_moves()
            for move in valid_moves:
                game.move(move, other_player)
                sim_eval = self.minimax(other_player, game, True)

                game.board[tuple(game.moves[move])] = ' '
                game.winner = None
                game.GameOver = False

                if sim_eval['score'] < min_eval['score']:
                    min_eval['score'] = sim_eval['score']
                    min_eval['move'] = move
            return min_eval
