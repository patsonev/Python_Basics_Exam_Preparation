count_players = int(input())

total_money = 0
count_total = 0
price = 0

for i in range(0, count_players):
    name_player = input()
    command = input()
    count_waffles = count_cakes = count_cookies = 0
    while command != 'Stop baking!':
        count_bake = int(input())
        count_total += count_bake
        kind_bake = command
        if kind_bake == 'cookies':
            price = 1.5
            count_cookies += count_bake
        elif kind_bake == 'cakes':
            price = 7.8
            count_cakes += count_bake
        elif kind_bake == 'waffles':
            price = 2.3
            count_waffles += count_bake
        total_money += count_bake * price
        command = input()
        if command == 'Stop baking!':
            break
    print(f'{name_player} baked {count_cookies} cookies, {count_cakes} cakes and {count_waffles} waffles.')

print(f'All bakery sold: {count_total}')
print(f'Total sum for charity: {total_money:.2f} lv.')