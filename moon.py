import math

mean_speed = float(input())
fuel_per_100 = float(input())

time = math.ceil(384400 * 2 / mean_speed + 3)
total_fuel = int(384400 * 2 * fuel_per_100 / 100)

print(time)
print(total_fuel)