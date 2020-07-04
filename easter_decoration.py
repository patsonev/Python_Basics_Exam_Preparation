count_clients = int(input())

total_sum = 0

for i in range(0, count_clients):
    bill = 0
    counter_product = 0
    product = ' '
    while product != 'Finish':
        product = input()
        if product == 'Finish':
            break
        if product == 'basket':
            bill += 1.5
            counter_product += 1
        if product == 'wreath':
            bill += 3.8
            counter_product += 1
        if product == 'chocolate bunny':
            bill += 7
            counter_product += 1
    if counter_product % 2 == 0:
        bill = bill * 0.8
    print(f'You purchased {counter_product} items for {bill:.2f} leva.')
    total_sum += bill

print(f'Average bill per client is: {total_sum / count_clients:.2f} leva.')