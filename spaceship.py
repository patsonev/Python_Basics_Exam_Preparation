import math

width = float(input())
length = float(input())
high = float(input())
mean_high = float(input())

volume_per_astronaut = 2 * 2 * (mean_high + 0.4)

volume_spaceship = width * length * high

count_rooms = volume_spaceship / volume_per_astronaut

if 3 <= count_rooms <= 10:
    print(f'The spacecraft holds {math.floor(count_rooms)} astronauts.')

elif count_rooms < 3:
    print(f'The spacecraft is too small.')

elif count_rooms > 10:
    print(f'The spacecraft is too big.')