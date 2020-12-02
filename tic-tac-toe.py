import random


def display_board(board):

    print('\n'*100)

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    marker = ''

    # Choose 'X' or 'O'
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: choose X or O: ').upper()

    if marker == 'X':

        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):

    board[position] = marker


def win_check(board, mark):

    return (board[1] == board[2] == board[3] == mark) or \
        (board[4] == board[5] == board[6] == mark) or \
        (board[7] == board[8] == board[9] == mark) or \
        (board[7] == board[4] == board[1] == mark) or \
        (board[8] == board[5] == board[2] == mark) or \
        (board[9] == board[6] == board[3] == mark) or \
        (board[7] == board[5] == board[3] == mark) or \
        (board[9] == board[5] == board[1] == mark)


def choose_first():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):

    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board):

    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Choose a position (1:9) '))

    return position


def replay():

    choice = input('Play again? Enter Yes or No? ')

    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

while True:

    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f'{turn} will go first')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has WON!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:

            if turn == 'Player 2':

                display_board(the_board)

                position = player_choice(the_board)

                place_marker(the_board, player2_marker, position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print('Player 2 has WON!!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print('Tie!')
                        game_on = False
                    else:
                        turn = 'Player 1'

    if not replay():
        break
