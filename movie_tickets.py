import math

a1 = int(input())
a2 = int(input())
n = int(input())

if a1 % 2 == 1:
    starting_number = a1
else:
    starting_number = a1 + 1

for i in range(starting_number, a2, 2):
    sign1 = str(chr(i))
    for sign2 in range(1, n):
        for sign3 in range(1, math.floor(n/2)):
            sign4 = i
            if (sign2 + sign3 + sign4) % 2 == 1:
                print(f'{sign1}-{sign2}{sign3}{sign4}')