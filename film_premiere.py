projection = input()
packet = input()
count_tickets = int(input())

if projection == 'John Wick':
    if packet == 'Drink':
        price = 12
    elif packet == 'Popcorn':
        price = 15
    elif packet == 'Menu':
        price = 19
elif projection == 'Star Wars':
    if packet == 'Drink':
        price = 18
    elif packet == 'Popcorn':
        price = 25
    elif packet == 'Menu':
        price = 30
elif projection == 'Jumanji':
    if packet == 'Drink':
        price = 9
    elif packet == 'Popcorn':
        price = 11
    elif packet == 'Menu':
        price = 14

if count_tickets >= 4 and projection == 'Star Wars':
    price *= 0.7
if count_tickets == 2 and projection == 'Jumanji':
    price *= 0.85

print(f'Your bill is {price * count_tickets:.2f} leva.')