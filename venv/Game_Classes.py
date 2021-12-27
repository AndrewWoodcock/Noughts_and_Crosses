
#   1   2   2
# a -   -   -
# b -   -   -
# c -   -   -

import re

class Board:
    def __init__(self, board_state):
        self.board_state = board_state

    def reset_board(self):
        for key, value in self.board_state.items():
            self.board_state[key] = ' '

    def display_board(self):
        print('  1|2|3' + '\n' +
              '--------' + '\n' +
              'A|'+ self.board_state['a1'] + '|' + self.board_state['a2'] + '|' + self.board_state['a3'] + '\n' +
              '--------' + '\n' +
              'B|'+ self.board_state['b1'] + '|' + self.board_state['b2'] + '|' + self.board_state['b3'] + '\n' +
              '--------' + '\n' +
              'C|'+ self.board_state['c1'] + '|' + self.board_state['c2'] + '|' + self.board_state['c3'] + '\n')

    def take_input(self, coord, player):
        if not re.search("[a-c][1-3]", coord):
            print(f'{coord} is not a valid input format, valid inputs are like "b1" or "c3"')
            return False
        elif self.board_state[coord] != ' ':
            print(f'{coord} is already populated, please pick again')
            return False
        else:
            self.board_state[coord] = player
            return True


    def check_win(self) -> bool:
        # win cases
        a_horiz = self.board_state['a1'] + self.board_state['a2'] + self.board_state['a3']
        b_horiz = self.board_state['b1'] + self.board_state['b2'] + self.board_state['b3']
        c_horiz = self.board_state['c1'] + self.board_state['c2'] + self.board_state['c3']
        vert_1 = self.board_state['a1'] + self.board_state['b1'] + self.board_state['c1']
        vert_2 = self.board_state['a2'] + self.board_state['b2'] + self.board_state['c2']
        vert_3 = self.board_state['a3'] + self.board_state['b3'] + self.board_state['c3']
        diag_down = self.board_state['a1'] + self.board_state['b2'] + self.board_state['c3']
        diag_up = self.board_state['c1'] + self.board_state['b2'] + self.board_state['a3']

        win_cases = [a_horiz, b_horiz, c_horiz, vert_1, vert_2, vert_3, diag_down, diag_up]

        for case in win_cases:
            if case == 'XXX':
                return True
            elif case == 'OOO':
                return True
            else:
                pass
        return False


class Scores:
    def __init__(self, games, X, O, draw):
        self.games = games
        self.X = X
        self.O = O
        self.draw = draw

    def show_scores(self):
        print('Scores:')
        print('X Wins: ' + str(self.X))
        print('O Wins: ' + str(self.O))
        print('Draws: ' + str(self.draw))