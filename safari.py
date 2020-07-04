budget = float(input())
count_litre = float(input())
day = input()

total_price = count_litre * 2.1 + 100

if day == 'Saturday':
    total_price *= 0.9
else:
    total_price *= 0.8

if total_price < budget:
    print(f'Safari time! Money left: {budget - total_price:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {total_price - budget:.2f} lv.')