count_tournirs = int(input())
starting_points = int(input())

sum_points = 0
counter = 0
points = 0

for i in range(0, count_tournirs):
    etap = input()
    if etap == 'W':
        points = 2000
        counter += 1
    elif etap == 'F':
        points = 1200
    elif etap == 'SF':
        points = 720
    sum_points += points

print(f'Final points: {starting_points + sum_points}')
print(f'Average points: {sum_points // count_tournirs}')
print(f'{counter * 100 / count_tournirs:.2f}%')