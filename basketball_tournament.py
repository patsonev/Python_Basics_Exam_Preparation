name_of_tournament = input()

counter_first = 0
counter_second = 0
counter_total = 0

while name_of_tournament != 'End of tournaments':
    count_games = int(input())
    for game in range(1, count_games + 1):
        first_team = int(input())
        second_team =int(input())
        counter_total += 1
        if first_team > second_team:
            print(f'Game {game} of tournament {name_of_tournament}: win with {first_team - second_team} points.')
            counter_first += 1
        else:
            print(f'Game {game} of tournament {name_of_tournament}: lost with {second_team - first_team} points.')
            counter_second += 1
    name_of_tournament = input()

print(f'{counter_first * 100 / counter_total:.2f}% matches win')
print(f'{counter_second * 100 / counter_total:.2f}% matches lost')