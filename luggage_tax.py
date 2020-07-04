width = int(input())
high = int(input())
length = int(input())
category = input()

volume = width * high * length
if volume <= 50:
    price = 0

if category == 'true':
    if 50 < volume <= 100:
        price = 0
    elif 100 < volume <= 200:
        price = 10
    elif 200 < volume <= 300:
        price = 20
else:
    if 50 < volume <= 100:
        price = 25
    elif 100 < volume <= 200:
        price = 50
    elif 200 < volume <= 300:
        price = 100

print(f'Luggage tax: {price:.2f}')