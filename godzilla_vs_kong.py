budget = float(input())
count_stats = int(input())
price_clothes = float(input())

price_dekor = 0.1 * budget

if count_stats > 150:
    price_clothes *= 0.9

total_price = count_stats * price_clothes + price_dekor

if total_price > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {total_price - budget:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {budget- total_price:.2f} leva left.')