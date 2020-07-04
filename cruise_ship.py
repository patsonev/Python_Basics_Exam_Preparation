kind_cruise = input()
kind_cabin = input()
nights = int(input())

if kind_cabin == 'standard cabin':
    if kind_cruise == 'Mediterranean':
        price = 27.5
    elif kind_cruise == 'Adriatic':
        price = 22.99
    elif kind_cruise == 'Aegean':
        price = 23
elif kind_cabin == 'cabin with balcony':
    if kind_cruise == 'Mediterranean':
        price = 30.2
    elif kind_cruise == 'Adriatic':
        price = 25
    elif kind_cruise == 'Aegean':
        price = 26.6
elif kind_cabin == 'apartment':
    if kind_cruise == 'Mediterranean':
        price = 40.5
    elif kind_cruise == 'Adriatic':
        price = 34.99
    elif kind_cruise == 'Aegean':
        price = 39.8

total_price = price * nights

if nights > 7:
    total_price = total_price * 0.75

print(f"Annie's holiday in the {kind_cruise} sea costs {total_price * 4:.2f} lv.")