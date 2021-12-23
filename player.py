import random
import math
class HumanPlayer:
    def __init__(self,letter):
        self.letter = letter


    def make_move(self, game):
        valid_move = False

        while not valid_move:
            move = input(self.letter + '\'s turn, Input move (0-8): ')
            try:
                valid_move = game.move(int(move), self.letter)
            except:
                pass

        return

  
class ComputerPlayer:
    def __init__(self, letter):
        self.letter = letter


    def make_move(self, game):
        moves = game.available_moves()
        move = random.choice(moves)
        game.move(move, self.letter)



class SmartComputerPlayer:
    def __init__(self, letter):
        self.letter = letter

    def make_move(self, game):

        if len(game.available_moves()) == 9:
            moves = game.available_moves()
            move = random.choice(moves)
            game.move(move, self.letter)
        
        else:
            other_player = 'O' if self.letter == 'X' else 'X'
            move = self.minimax(other_player, game, True)['move']

            game.move(move, self.letter)

    def minimax(self, other_player, game, MaximizingPlayer):
        if game.GameOver:
            moves_left = len(game.available_moves())
            if game.winner == None and moves_left == 0:
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

