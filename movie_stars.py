budget = float(input())

while budget > 0:
    name = input()
    if name == 'ACTION':
        break
    if len(name) > 15:
        price = 0.2 * budget
    else:
        price = float(input())
    budget -= price

if budget < 0:
    print(f'We need {abs(budget):.2f} leva for our actors.')
else:
    print(f'We are left with {budget:.2f} leva.')
