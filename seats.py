count_tickets = int(input())
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
decoded = ' '

for i in range(0, count_tickets):
    number_ticket = input()
    length = len(number_ticket)
    if length == 4:
        if number_ticket[0] in alphabet:
            decoded = number_ticket[0] + number_ticket[1] + number_ticket[2]
            print(f'Seat decoded: {decoded}')
        else:
            decoded = number_ticket[3] + number_ticket[1] + number_ticket[2]
            print(f'Seat decoded: {decoded}')
    else:
        decoded = number_ticket[0] + str(ord(number_ticket[1]))
        print(f'Seat decoded: {decoded}')