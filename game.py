'''
GAME
'''

def display_game(game_list):

    print('Here is the current list: ')
    print(game_list)


def position_coice():

    choice = 'wrong'

    while choice not in ['0', '1', '2']:

        choice = input('Pick a position (0, 1, 2): ')

        if choice not in ['0', '1', '2']:
            print('Sorry, invalid choice')

    return int(choice)


def replacement_choice(game_list, position):

    user_placement = input('Type a string to plce at position: ')

    game_list[position] = user_placement

    return game_list


def gameon_choice():

    choice = 'wrong'

    while choice not in ['Y', 'N']:

        choice = input('Keep playing? (Y or N) ')

        if choice not in ['Y', 'N']:
            print('Sorry, please choose Y or N')

    if choice == 'Y':
        return True
    else:
        return False


if __name__ == "__main__":
    game_on = True
    game_list = [0, 1, 2]

    while game_on:

        display_game(game_on)

        position = position_coice()

        game_list = replacement_choice(game_list, position)

        display_game(game_list)

        game_on = gameon_choice()
