destination = input()
date = input()
count_nights = int(input())

if destination == 'France':
    if date == '21-23':
        price_night = 30
    elif date == '24-27':
        price_night = 35
    elif date == '28-31':
        price_night = 40
elif destination == 'Italy':
    if date == '21-23':
        price_night = 28
    elif date == '24-27':
        price_night = 32
    elif date == '28-31':
        price_night = 39
elif destination == 'Germany':
    if date == '21-23':
        price_night = 32
    elif date == '24-27':
        price_night = 37
    elif date == '28-31':
        price_night = 43

print(f'Easter trip to {destination} : {price_night * count_nights:.2f} leva.')