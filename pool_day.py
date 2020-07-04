import math

count_people = int(input())
fee = float(input())
price_shezlong = float(input())
price_umbrella = float(input())

count_shezlong = math.ceil(count_people * 0.75)
count_umbrella = math.ceil(count_people / 2)

total = count_people * fee + count_umbrella * price_umbrella + count_shezlong * price_shezlong

print(f'{total:.2f} lv.')