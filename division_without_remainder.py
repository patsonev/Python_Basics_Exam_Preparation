count_numbers = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(0, count_numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1

print(f'{p1 * 100 / count_numbers:.2f}%')
print(f'{p2 * 100 / count_numbers:.2f}%')
print(f'{p3 * 100 / count_numbers:.2f}%')