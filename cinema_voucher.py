voucher = int(input())

counter_tickets = 0
counter_others = 0

while voucher > 0:
    item = input()
    if item == 'End':
        break
    length_name_item = len(item)
    if length_name_item > 8:
        price_item = ord(item[0]) + ord(item[1])
        if price_item <= voucher:
            voucher -= price_item
            counter_tickets += 1
        else:
            break
    else:
        price_item = ord(item[0])
        if price_item <= voucher:
            voucher -= price_item
            counter_others += 1
        else:
            break

print(counter_tickets)
print(counter_others)