count_days = int(input())
count_hours = int(input())

total_price = 0

for p in range(1, count_days + 1):
    day_price = 0
    for q in range(1, count_hours + 1):
        if p % 2 == 1 and q % 2 == 0:
            price = 1.25
        elif p % 2 == 0 and q % 2 == 1:
            price = 2.5
        else:
            price = 1
        day_price += price
    total_price += day_price
    print(f'Day: {p} - {day_price:.2f} leva')

print(f'Total: {total_price:.2f} leva')