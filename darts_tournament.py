starting_points = int(input())
sector = ' '

counter = 0

while starting_points != 0:
    sector = input()
    counter += 1
    if sector == 'bullseye':
        print(f'Congratulations! You won the game with a bullseye in {counter} moves!')
        break
    current_points = int(input())
    if sector == 'double ring':
        current_points = current_points * 2
    elif sector == 'triple ring':
        current_points = current_points * 3
    starting_points -= current_points
    if starting_points < 0:
        print(f'Sorry, you lost. Score difference: {abs(starting_points)}.')
        break
    elif starting_points == 0:
        print(f'Congratulations! You won the game in {counter} moves!')
        break
