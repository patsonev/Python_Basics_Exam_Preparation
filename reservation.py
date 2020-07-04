day_reservation = int(input())
month_reservation = int(input())
day_starting = int(input())
month_starting = int(input())
day_ending = int(input())
month_ending = int(input())

price = 30

if day_starting - day_reservation > 10:
    price = 25
if month_starting > month_reservation:
    price = 20

total_price = (day_ending - day_starting) * price
print(f'Your stay from {day_starting}/{month_starting} to {day_ending}/{month_ending} will cost {total_price:.2f}')