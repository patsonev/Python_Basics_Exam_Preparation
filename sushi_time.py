import math

kind_sushi = input()
name_restourant = input()
count_portions = int(input())
dostavka = input()

price = 0

if name_restourant == 'Sushi Zone':
    if kind_sushi == 'sashimi':
        price = 4.99
    elif kind_sushi == 'maki':
        price = 5.29
    elif kind_sushi == 'uramaki':
        price = 5.99
    elif kind_sushi == 'temaki':
        price = 4.29
    total_price = price * count_portions
    if dostavka == 'Y':
        total_price = 1.2 * total_price
    print(f'Total price: {math.ceil(total_price)} lv.')

elif name_restourant == 'Sushi Time':
    if kind_sushi == 'sashimi':
        price = 5.49
    elif kind_sushi == 'maki':
        price = 4.69
    elif kind_sushi == 'uramaki':
        price = 4.49
    elif kind_sushi == 'temaki':
        price = 5.19
    total_price = price * count_portions
    if dostavka == 'Y':
        total_price = 1.2 * total_price
    print(f'Total price: {math.ceil(total_price)} lv.')

elif name_restourant == 'Sushi Bar':
    if kind_sushi == 'sashimi':
        price = 5.25
    elif kind_sushi == 'maki':
        price = 5.55
    elif kind_sushi == 'uramaki':
        price = 6.25
    elif kind_sushi == 'temaki':
        price = 4.75
    total_price = price * count_portions
    if dostavka == 'Y':
        total_price = 1.2 * total_price
    print(f'Total price: {math.ceil(total_price)} lv.')

elif name_restourant == 'Asian Pub':
    if kind_sushi == 'sashimi':
        price = 4.5
    elif kind_sushi == 'maki':
        price = 4.8
    elif kind_sushi == 'uramaki':
        price = 5.5
    elif kind_sushi == 'temaki':
        price = 5.5
    total_price = price * count_portions
    if dostavka == 'Y':
        total_price = 1.2 * total_price
    print(f'Total price: {math.ceil(total_price)} lv.')

else:
    print(f'{name_restourant} is invalid restaurant!')