trip_days = int(input())

budget = 60
counter = 0

for i in range(0, trip_days):
    while budget != 0:
        command = input()
        if command == 'Day over':
            break
        else:
            day_money = float(command)
            counter += 1
            budget -= day_money
    money_left = budget
    if budget == 0:
        print(f"Daily limit exceeded! You've bought {counter} products.")
    else:
        print(f"Money left from today: {money_left:.2f}. You've bought {counter} products.")
    budget = 60 + money_left
    counter = 0