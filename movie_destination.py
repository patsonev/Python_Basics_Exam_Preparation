movie_budget = float(input())
destination = input()
season = input()
count_days = int(input())

if season == 'Winter':
    if destination == 'Dubai':
        price = 45000 * 0.7
    elif destination == 'Sofia':
        price = 17000 * 1.25
    elif destination == 'London':
        price = 24000
elif season == 'Summer':
    if destination == 'Dubai':
        price = 40000 * 0.7
    elif destination == 'Sofia':
        price = 12500 * 1.25
    elif destination == 'London':
        price = 20250

needed_money = count_days * price

if needed_money <= movie_budget:
    print(f'The budget for the movie is enough! We have {movie_budget - needed_money:.2f} leva left!')
else:
    print(f'The director needs {needed_money - movie_budget:.2f} leva more!')