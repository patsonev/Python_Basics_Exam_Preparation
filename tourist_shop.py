budget = float(input())
command = input()

counter = 0
total_price = 0

while command != 'Stop':
    counter += 1
    price = float(input())
    if counter % 3 == 0:
        price *= 0.5
    total_price += price
    if total_price > budget:
        print(f"You don't have enough money!")
        print(f'You need {total_price - budget:.2f} leva!')
        break
    command = input()

if command == 'Stop':
    print(f'You bought {counter} products for {total_price:.2f} leva.')