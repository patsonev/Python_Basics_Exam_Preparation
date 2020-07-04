size_egg = input()
color_egg = input()
count_eggs = int(input())

if size_egg == 'Large':
    if color_egg == 'Red':
        price = 16
    elif color_egg == 'Green':
        price = 12
    elif color_egg == 'Yellow':
        price = 9
elif size_egg == 'Medium':
    if color_egg == 'Red':
        price = 13
    elif color_egg == 'Green':
        price = 9
    elif color_egg == 'Yellow':
        price = 7
elif size_egg == 'Small':
    if color_egg == 'Red':
        price = 9
    elif color_egg == 'Green':
        price = 8
    elif color_egg == 'Yellow':
        price = 5

print(f'{(price * count_eggs) * 0.65:.2f} leva.')
