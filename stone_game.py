from random import randint
import sys

player_name1 = input('Enter name of player №1:\t').title()
player_name2 = input('Enter name of player №2:\t').title()

N = randint(4, 30)

while True:
    print(f'\n{player_name1} turn...')
    print(f'Current quantity:\t{N}')
    n = int(input('Enter a number from 1 to 3:\t'))
    N -= n
    if N < 1:
        sys.exit(f'{player_name1} lost!')

    print(f'\n{player_name2} turn...')
    print(f'Current quantity:\t{N}')
    n = int(input('Enter a number from 1 to 3:\t'))
    N -= n
    if N < 1:
        sys.exit(f'{player_name2} lost!')
