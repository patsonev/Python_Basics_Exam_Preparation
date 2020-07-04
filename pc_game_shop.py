count_games = int(input())

counter_hearthstone = 0
counter_fornite = 0
counter_overwatch = 0
counter_others = 0

for i in range(count_games):
    game_name = input()
    if game_name == 'Hearthstone':
        counter_hearthstone += 1
    elif game_name == 'Fornite':
        counter_fornite += 1
    elif game_name == 'Overwatch':
        counter_overwatch += 1
    else:
        counter_others += 1

print(f'Hearthstone - {100 * counter_hearthstone / count_games:.2f}%')
print(f'Fornite - {100 * counter_fornite / count_games:.2f}%')
print(f'Overwatch - {100 * counter_overwatch / count_games:.2f}%')
print(f'Others - {100 * counter_others / count_games:.2f}%')