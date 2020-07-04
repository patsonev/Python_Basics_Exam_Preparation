number_ticket = input()
price_ticket = float(input())
minutes_waiting = int(input())

min_waiting = minutes_waiting
last_ticket_number = number_ticket
last_ticket_price = price_ticket

while number_ticket != 'End':
    if minutes_waiting < min_waiting:
        last_ticket_number = number_ticket
        last_ticket_price = price_ticket
        min_waiting = minutes_waiting
    number_ticket = input()
    if number_ticket == 'End':
        break
    price_ticket = float(input())
    minutes_waiting = int(input())

price_lv = last_ticket_price * 1.96

print(f'Ticket found for flight {last_ticket_number} costs {price_lv:.2f} leva with {min_waiting // 60}h {min_waiting % 60}m stay')