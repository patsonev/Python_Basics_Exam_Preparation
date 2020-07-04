budget = float(input())
count_videocards = int(input())
count_processors = int(input())
count_ram = int(input())

price_videocard = 250
total_price_videocards = count_videocards * price_videocard
price_processor = 0.35 * total_price_videocards
price_ram = 0.1 * total_price_videocards

total_price = price_videocard * count_videocards + price_processor * count_processors + price_ram * count_ram

if count_videocards > count_processors:
    total_price *= 0.85

if budget >= total_price:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')