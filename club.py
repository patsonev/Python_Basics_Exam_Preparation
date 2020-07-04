needed_money = float(input())

income = 0

while needed_money > income:
    name_cocktail = input()
    if name_cocktail == 'Party!':
        break
    count_cocktails = int(input())
    price = len(name_cocktail)
    price_total = price * count_cocktails
    if price_total % 2 == 1:
        price_total *= 0.75
    income += price_total

if income >= needed_money:
    print(f'Target acquired.')
else:
    print(f'We need {needed_money - income:.2f} leva more.')

print(f'Club income - {income:.2f} leva.')