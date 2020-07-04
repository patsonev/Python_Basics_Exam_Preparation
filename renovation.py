import math

high = int(input())
width = int(input())
percent_from_total = int(input())

total = math.ceil(high * width * 4 * (100 - percent_from_total) / 100)

while total >= 0:
    command = input()
    if command == 'Tired!':
        break
    litre_paint = int(command)
    total -= litre_paint
    if total == 0:
        print(f'All walls are painted! Great job, Pesho!')
        break

if total > 0:
    print(f'{int(total)} quadratic m left.')
if total < 0:
    print(f'All walls are painted and you have {int(-total)} l paint left!')