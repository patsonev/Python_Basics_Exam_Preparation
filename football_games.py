count_w = 0
count_d = 0
count_l = 0

for i in range(3):
    result = input()
    if int(result[0]) > int(result[2]):
        count_w += 1
    elif int(result[0]) < int(result[2]):
        count_l += 1
    else:
        count_d += 1

print(f'Team won {count_w} games.')
print(f'Team lost {count_l} games.')
print(f'Drawn games: {count_d}')