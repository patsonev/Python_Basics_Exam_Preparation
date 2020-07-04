destination = input()
date_reservation = input()
count_nights = int(input())

if destination == "France":
    if date_reservation == "21-23":
        price = 30
    elif date_reservation == "24-27":
        price = 35
    elif date_reservation == "28-31":
        price = 40

elif destination == "Italy":
    if date_reservation == "21-23":
        price = 28
    elif date_reservation == "24-27":
        price = 32
    elif date_reservation == "28-31":
        price = 39

elif destination == "Germany":
    if date_reservation == "21-23":
        price = 32
    elif date_reservation == "24-27":
        price = 37
    elif date_reservation == "28-31":
        price = 43

total_price = price * count_nights

print(f"Easter trip to {destination} : {total_price:.2f} leva.")