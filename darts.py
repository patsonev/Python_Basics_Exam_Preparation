name = input()

is_zero = False

counter_points = 301
counter_rounds = 0
counter_unsuccessful = 0

while not is_zero:
    sector = input()
    if sector == 'Retire':
        print(f'{name} retired after {counter_unsuccessful} unsuccessful shots.')
        is_zero = True
        continue
    points = int(input())
    counter_rounds += 1
    if sector == 'Triple':
        points = 3 * points
    elif sector == 'Double':
        points = points * 2
    if counter_points - points < 0:
        counter_unsuccessful += 1
        continue
    counter_points -= points
    if counter_points == 0:
        print(f'{name} won the leg with {counter_rounds - counter_unsuccessful} shots.')
        is_zero = True