command = input()

total_tickets = 0
counter_students = 0
counter_standard = 0
counter_kid = 0

while command != 'Finish':
    counter_seats = 0
    count_seats = int(input())
    while counter_seats < count_seats:
        kind_ticket = input()
        if kind_ticket == 'student':
            counter_students += 1
        elif kind_ticket == 'standard':
            counter_standard += 1
        elif kind_ticket == 'kid':
            counter_kid += 1
        else:
            break
        counter_seats += 1
    print(f'{command} - {counter_seats * 100 / count_seats:.2f}% full.')
    total_tickets += counter_seats
    command = input()

print(f'Total tickets: {total_tickets}')
print(f'{counter_students * 100 / total_tickets:.2f}% student tickets.')
print(f'{counter_standard * 100 / total_tickets:.2f}% standard tickets.')
print(f'{counter_kid * 100 / total_tickets:.2f}% kids tickets.')