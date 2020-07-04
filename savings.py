income = float(input())
months = int(input())
needed_per_month = float(input())

saved_money = (0.7 * income - needed_per_month) * months

print(f'She can save {saved_money * 100 / (income * months):.2f}%')
print(f'{saved_money:.2f}')