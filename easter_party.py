guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= guests <= 15:
    price_per_person = price_per_person * 0.85
elif 15 < guests <= 20:
    price_per_person = price_per_person * 0.80
elif guests > 20:
    price_per_person = price_per_person * 0.75

cena = guests * price_per_person + 0.1 * budget

if cena <= budget:
    print(f'It is party time! {budget - cena:.2f} leva left.')
else:
    print(f'No party! {cena - budget:.2f} leva needed.')