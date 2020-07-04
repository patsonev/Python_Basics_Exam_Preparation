count_chicken = int(input())
count_fish = int(input())
count_vegan = int(input())

total_sum = (count_chicken * 10.35 + count_fish * 12.4 + count_vegan * 8.15) * 1.2 + 2.5

print(f'Total: {total_sum:.2f}')