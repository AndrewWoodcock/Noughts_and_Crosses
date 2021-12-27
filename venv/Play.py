
from Game_Classes import Board, Scores


def build_new_board() -> Board:
    new_board = Board({'a1': ' ', 'a2': ' ', 'a3': ' ',
                       'b1': ' ', 'b2': ' ', 'b3': ' ',
                       'c1': ' ', 'c2': ' ', 'c3': ' '})
    return new_board


def play_game(board: Board, game_score: Scores):
    finish_state = False
    win_state = False
    X = True
    O = False

    while win_state * finish_state == 0:
        if X is True:
            # store the user input
            good_input = False
            while good_input is False:
                coord = input('Xs Please pick input: ')
                good_input = board.take_input(coord, 'X')
            # check if there is a win
            win_state = board.check_win()
            X, O = False, True

            board.display_board()
            if win_state is True:
                print('Xs Win!')
                game_score.X += 1
                play_again = input('Would you like to play again (y/n)?')
                if play_again == 'y':
                    finish_state = False
                    print('\n')
                    game_score.show_scores()
                    board.reset_board()
                    print('\n')
                    board.display_board()
                else:
                    finish_state = True
                    print('\n Final Scores:')
                    game_score.show_scores()
        else:
            # store the user input
            good_input = False
            while good_input is False:
                coord = input('Os Please pick input: ')
                good_input = board.take_input(coord, 'O')
            win_state = board.check_win()
            X, O = True, False

            board.display_board()
            if win_state is True:
                print('Os Win!')
                game_score.O += 1
                play_again = input('Would you like to play again (y/n)?')
                if play_again == 'y':
                    finish_state = False
                    print('\nCurrent Scores')
                    game_score.show_scores()
                    board.reset_board()
                    print('\n')
                    board.display_board()
                else:
                    finish_state = True
                    print('\n')
                    game_score.show_scores()

def main():
    # set up the new game
    print('\nStarting New Game \n')
    board = build_new_board()
    board.display_board()
    game_score = Scores(0, 0, 0, 0)
    game_score.show_scores()

    # player_1 = X, player_2 = O
    print('\nXs go first')
    print('Inputs must be in form a#, b#, c#, example: "a1" or "b3"')
    play_game(board, game_score)

    # need to find a way to check if a win is still possible, if not draw should be called to end the game

if __name__ == '__main__':
    main()