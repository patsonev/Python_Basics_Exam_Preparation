etap = input()
kind_of_ticket = input()
count_tickets = int(input())
photo = input()

price = 0

if etap == 'Quarter final':
    if kind_of_ticket == 'Standard':
        price = 55.5
    elif kind_of_ticket == 'Premium':
        price = 105.2
    elif kind_of_ticket == 'VIP':
        price = 118.9
if etap == 'Semi final':
    if kind_of_ticket == 'Standard':
        price = 75.88
    elif kind_of_ticket == 'Premium':
        price = 125.22
    elif kind_of_ticket == 'VIP':
        price = 300.4
if etap == 'Final':
    if kind_of_ticket == 'Standard':
        price = 110.1
    elif kind_of_ticket == 'Premium':
        price = 160.66
    elif kind_of_ticket == 'VIP':
        price = 400

total = price * count_tickets

if total > 4000:
    total = total * 0.75
    print(f'{total:.2f}')
elif 4000 >= total > 2500:
    total = total * 0.9
    if photo == 'Y':
        total += count_tickets * 40
    print(f'{total:.2f}')
else:
    if photo == 'Y':
        total += count_tickets * 40
    print(f'{total:.2f}')