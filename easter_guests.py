count_guests = int(input())
budget = int(input())

count_eggs = count_guests * 2
remain = count_guests % 3

if remain == 0:
    count_cakes = count_guests / 3
else:
    count_cakes = count_guests // 3 + 1

total_price = count_eggs * 0.45 + count_cakes * 4

if budget >= total_price:
    print(f'Lyubo bought {int(count_cakes)} Easter bread and {count_eggs} eggs.')
    print(f'He has {budget - total_price:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")