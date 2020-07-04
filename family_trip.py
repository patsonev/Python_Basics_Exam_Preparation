budget = float(input())
count_nights = int(input())
price_night = float(input())
percent_additional = int(input())

if count_nights > 7:
    price_night *= 0.95

total_price = percent_additional * budget / 100 + count_nights * price_night

if total_price <= budget:
    print(f'Ivanovi will be left with {budget - total_price:.2f} leva after vacation.')
else:
    print(f'{total_price - budget:.2f} leva needed.')