team_name = input()
count_games = int(input())

count_w = 0
count_d = 0
count_l = 0
points = 0

for i in range(count_games):
    game_result = input()
    if game_result == 'W':
        count_w += 1
        points += 3
    elif game_result == 'D':
        count_d += 1
        points += 1
    elif game_result == 'L':
        count_l += 1

if count_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {count_w}")
    print(f"## D: {count_d}")
    print(f"## L: {count_l}")
    print(f"Win rate: {100 * count_w / count_games:.2f}%")