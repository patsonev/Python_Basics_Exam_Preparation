counter_wins = 0
counter_loses = 0
counter_drawns = 0

for i in range(0, 3):
    result = input()
    first = int(result[0])
    second = int(result[2])
    if first == second:
        counter_drawns += 1
    elif first > second:
        counter_wins += 1
    elif first < second:
        counter_loses += 1

print(f'Team won {counter_wins} games.')
print(f'Team lost {counter_loses} games.')
print(f'Drawn games: {counter_drawns}')
