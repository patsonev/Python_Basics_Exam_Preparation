kind_coffee = input()
sugar = input()
count_coffees = int(input())

if kind_coffee == 'Espresso':
    if sugar == 'Without':
        price = 0.9
    elif sugar == 'Normal':
        price = 1
    elif sugar == 'Extra':
        price = 1.2

elif kind_coffee == 'Cappuccino':
    if sugar == 'Without':
        price = 1
    elif sugar == 'Normal':
        price = 1.2
    elif sugar == 'Extra':
        price = 1.6

elif kind_coffee == 'Tea':
    if sugar == 'Without':
        price = 0.5
    elif sugar == 'Normal':
        price = 0.6
    elif sugar == 'Extra':
        price = 0.7

total_price = count_coffees * price

if sugar == 'Without':
    total_price *= 0.65

if kind_coffee == 'Espresso' and count_coffees >= 5:
    total_price *= 0.75

if total_price > 15:
    total_price *= 0.8

print(f'You bought {count_coffees} cups of {kind_coffee} for {total_price:.2f} lv.')