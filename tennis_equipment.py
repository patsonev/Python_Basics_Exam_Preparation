import math

price_tennis_rocket = float(input())
count_tennis_rocket = int(input())
count_trousers = int(input())

price_trousers = price_tennis_rocket / 6

price =  count_tennis_rocket * price_tennis_rocket + count_trousers * price_trousers
total_price = price + price * 0.2

print(f'Price to be paid by Djokovic {int(total_price // 8)}')
print(f'Price to be paid by sponsors {math.ceil(total_price * 7 / 8)}')