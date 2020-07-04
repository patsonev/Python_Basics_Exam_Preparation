name = input()
count_games = int(input())

total_points_volleyball = 0
total_points_tennis = 0
total_points_badminton = 0

counter_volleyball = 0
counter_tennis = 0
counter_badminton = 0

for i in range(0, count_games):
    game_name = input()
    points = int(input())
    if game_name == 'volleyball':
        points = points + points * 0.07
        total_points_volleyball += points
        counter_volleyball += 1
    elif game_name == 'tennis':
        points = points + 0.05 * points
        total_points_tennis += points
        counter_tennis += 1
    elif game_name == 'badminton':
        points = points + 0.02 * points
        total_points_badminton += points
        counter_badminton += 1

if counter_volleyball != 0:
    mean_volleyball = total_points_volleyball // counter_volleyball
else:
    mean_volleyball = 75

if counter_tennis != 0:
    mean_tennis = total_points_tennis // counter_tennis
else:
    mean_tennis = 75

if counter_badminton != 0:
    mean_badminton = total_points_badminton // counter_badminton
else:
    mean_badminton = 75

total_points = total_points_tennis + total_points_badminton + total_points_volleyball

if mean_badminton >= 75 and mean_tennis >= 75 and mean_volleyball >= 75:
    print(f'Congratulations, {name}! You won the cruise games with {int(total_points // 1)} points.')
else:
    print(f'Sorry, {name}, you lost. Your points are only {int(total_points // 1)}.')