country = input()
discipline = input()
points = 0

if country == 'Russia':
    if discipline == 'ribbon':
        points = 18.5
    elif discipline == 'hoop':
        points = 19.1
    elif discipline == 'rope':
        points = 18.6
elif country == 'Bulgaria':
    if discipline == 'ribbon':
        points = 19
    elif discipline == 'hoop':
        points = 19.3
    elif discipline == 'rope':
        points = 18.9
elif country == 'Italy':
    if discipline == 'ribbon':
        points = 18.7
    elif discipline == 'hoop':
        points = 18.8
    elif discipline == 'rope':
        points = 18.85

print(f'The team of {country} get {points:.3f} on {discipline}.')
print(f'{(1 - points / 20) * 100:.2f}%')