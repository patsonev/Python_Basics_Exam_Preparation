count_bakes = int(input())

counter_sugar = 0
counter_flour = 0

max_sugar = 0
max_flour = 0

for i in range(0, count_bakes):
    needed_sugar = int(input())
    needed_flour = int(input())
    counter_sugar += needed_sugar
    counter_flour += needed_flour
    if needed_sugar > max_sugar:
        max_sugar = needed_sugar
    if needed_flour > max_flour:
        max_flour = needed_flour

remain_sugar = counter_sugar % 950
if remain_sugar != 0:
    packets_sugar = counter_sugar // 950 + 1
else:
    packets_sugar = counter_sugar // 950

remain_flour = counter_flour % 750
if remain_flour != 0:
    packets_flour = counter_flour // 750 + 1
else:
    packets_flour = counter_flour // 750

print(f'Sugar: {(packets_sugar)}')
print(f'Flour: {(packets_flour)}')
print(f'Max used flour is {(max_flour)} grams, max used sugar is {(max_sugar)} grams.')