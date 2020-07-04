duration_contract = input()
kind_contract = input()
mobile_internet = input()
count_months = int(input())

if duration_contract == 'one':
    if kind_contract == 'Small':
        tax = 9.98
    elif kind_contract == 'Middle':
        tax = 18.99
    elif kind_contract == 'Large':
        tax = 25.98
    elif kind_contract == 'ExtraLarge':
        tax = 35.99

elif duration_contract == 'two':
    if kind_contract == 'Small':
        tax = 8.58
    elif kind_contract == 'Middle':
        tax = 17.09
    elif kind_contract == 'Large':
        tax = 23.59
    elif kind_contract == 'ExtraLarge':
        tax = 31.79

if mobile_internet == 'yes':
    if tax <= 10:
        tax += 5.5
    elif 10 < tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85

if duration_contract == 'two':
    tax = tax * (1 - 0.0375)

print(f'{count_months * tax:.2f} lv.')
