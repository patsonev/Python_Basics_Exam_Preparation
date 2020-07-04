counter_bake = int(input())
max_grade = 0

for i in range(0, counter_bake):
    chef = input()
    count_grade = 0
    sum_grade = 0
    is_stop = False
    while not is_stop:
        command = input()
        if command == 'Stop':
            is_stop = True
            break
        grade = int(command)
        count_grade += 1
        sum_grade += grade
    print(f'{chef} has {sum_grade} points.')
    if sum_grade > max_grade:
        champion = chef
        max_grade = sum_grade
        print(f'{chef} is the new number 1!')

print(f'{champion} won competition with {max_grade} points!')