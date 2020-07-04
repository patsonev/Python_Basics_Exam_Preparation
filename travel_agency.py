city_name = input()
kind = input()
vip = input()
days = int(input())

is_correct = False

if days > 7:
    days -= 1

if city_name == 'Bansko':
    if kind == 'noEquipment':
        price = 80
        is_correct = True
        if vip == 'yes':
            price *= 0.95
    elif kind == 'withEquipment':
        price = 100
        is_correct = True
        if vip == 'yes':
            price *= 0.9

elif city_name == 'Borovets':
    if kind == 'noEquipment':
        price = 80
        is_correct = True
        if vip == 'yes':
            price *= 0.95
    elif kind == 'withEquipment':
        price = 100
        is_correct = True
        if vip == 'yes':
            price *= 0.9

elif city_name == 'Varna':
    if kind == 'noBreakfast':
        price = 100
        is_correct = True
        if vip == 'yes':
            price *= 0.93
    elif kind == 'withBreakfast':
        price = 130
        is_correct = True
        if vip == 'yes':
            price *= 0.88

elif city_name == 'Burgas':
    if kind == 'noBreakfast':
        price = 100
        is_correct = True
        if vip == 'yes':
            price *= 0.93
    elif kind == 'withBreakfast':
        price = 130
        is_correct = True
        if vip == 'yes':
            price *= 0.88

if days < 1:
    is_correct = False

if is_correct:
    print(f'The price is {price * days:.2f}lv! Have a nice time!')

if is_correct is False and days < 1:
    print(f'Days must be positive number!')

if is_correct is False and days >= 1:
    print(f'Invalid input!')