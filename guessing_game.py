from random import randint

secret_num = randint(0, 100)

print()
print()
print('GUESS THE NUMBER')
print('================')
print()
print('RULES:')
print('================')
print('Computer picks random number between 0 and 100')
print('The player makes a guess what the number is')
print('If a player\'s guess is less than 1 or greater than 100, say "OUT OF BOUNDS"')
print('On a player\'s first turn, if their guess is')
print('Within 10 of the number, return "WARM!"')
print('further than 10 away from the number, return "COLD!"')
print('On all subsequent turns, if a guess is')
print('closer to the number than the previous guess return "WARMER!"')
print('farther from the number than the previous guess, return "COLDER!"')
print('When the player\'s guess equals the number, tell them they\'ve')
print('guessed correctly and how many guesses it took!')

guesses_list = 0
number_guessed = False

guess = int(input('Please type a number between 0 and 100 here! '))

if guess == secret_num:
    number_guessed = True
    guesses_list = []
    guesses_list.append(guess)

while not guess == secret_num:

    if not 0 <= guess <= 100:
        print('OUT OF BOUNDS')

        guess = int(input('Type again '))
        continue

    if not guesses_list:
        guesses_list = []
        guesses_list.append(guess)

        if guess == secret_num:
            number_guessed = True
            break

        elif abs(guess - secret_num) <= 10:
            print('WARM')
        elif abs(guess - secret_num) > 10:
            print('COLD')

        guess = int(input('Type again '))
        continue

    guesses_list.append(guess)

    if abs(guesses_list[-1] - secret_num) < abs(guesses_list[-2] - secret_num):
        print('WARMER')
    elif abs(guesses_list[-1] - secret_num) > abs(guesses_list[-2] - secret_num):
        print('COLDER')

    guess = int(input('Type again '))
    if guess == secret_num:
        guesses_list.append(guess)
        number_guessed = True
        break

if number_guessed:
    print('Congratulations you\'ve guessed the number!')
    print(f'The number was {secret_num}!')
    print(f'You guessed the number in {len(guesses_list)} guesses.')
