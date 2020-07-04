first_range = int(input())
second_range = int(input())
third_range = int(input())

for i in range(1, first_range + 1):
    for j in range(1, second_range + 1):
        for k in range(1, third_range + 1):
            if i % 2 == 0 and k % 2 == 0 and (j == 7 or j == 5 or j == 3 or j == 2):
                print(f'{i} {j} {k}')