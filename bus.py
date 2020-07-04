count_passengers = int(input())
count_stations = int(input())

for i in range(1, count_stations + 1):
    passenger_out = int(input())
    passenger_in = int(input())
    count_passengers = count_passengers + passenger_in - passenger_out
    if i % 2 == 1:
        count_passengers += 2
    else:
        count_passengers -= 2

print(f'The final number of passengers is : {count_passengers}')