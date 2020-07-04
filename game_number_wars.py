first_name = input()
second_name = input()

first_points = 0
second_points = 0

is_play = True

while is_play:
    first_card = input()
    if first_card == 'End of game':
        print(f'{first_name} has {first_points} points')
        print(f'{second_name} has {second_points} points')
        is_play = False
        break
    second_card = input()
    first_to_number = int(first_card)
    second_to_number = int(second_card)
    if first_to_number > second_to_number:
        first_points += abs(first_to_number - second_to_number)
    elif first_to_number < second_to_number:
        second_points += abs(first_to_number - second_to_number)
    else:
        first_to_number = int(input())
        second_to_number = int(input())
        if first_to_number > second_to_number:
            print(f'Number wars!')
            print(f'{first_name} is winner with {first_points} points')
            is_play = False
            break
        else:
            print(f'Number wars!')
            print(f'{second_name} is winner with {second_points} points')
            is_play = False
            break