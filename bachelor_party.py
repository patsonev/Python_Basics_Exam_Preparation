money_for_singer = int(input())
command = input()

counter_guests = 0
income = 0

while command != 'The restaurant is full':
    count_guests = int(command)
    counter_guests += count_guests
    if count_guests < 5:
        price = 100
    else:
        price = 70
    income += count_guests * price
    command = input()

if income >= money_for_singer:
    print(f'You have {counter_guests} guests and {income - money_for_singer} leva left.')
else:
    print(f'You have {counter_guests} guests and {income} leva income, but no singer.')
