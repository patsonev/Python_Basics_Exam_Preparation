kg_lemons = float(input())
kg_sugar = float(input())
water = float(input())

total_lemon_juice = kg_lemons * 980 + kg_sugar * 0.3 + water * 1000
total_cups = total_lemon_juice // 150
money_earned = total_cups * 1.2

print(f'All cups sold: {int(total_cups)}')
print(f'Money earned: {money_earned:.2f}')