count_eggs = int(input())

counter_red = 0
counter_orange = 0
counter_blue = 0
counter_green = 0

for i in range(1, count_eggs + 1):
    color = input()
    if color == 'red':
        counter_red += 1
    elif color == 'orange':
        counter_orange += 1
    elif color == 'blue':
        counter_blue += 1
    elif color == 'green':
        counter_green += 1

max_number = counter_red
color = 'red'
if counter_orange > max_number:
    max_number = counter_orange
    color = 'orange'
if counter_blue > max_number:
    max_number = counter_blue
    color = 'blue'
if counter_green > max_number:
    max_number = counter_green
    color = 'green'

print(f'Red eggs: {counter_red}')
print(f'Orange eggs: {counter_orange}')
print(f'Blue eggs: {counter_blue}')
print(f'Green eggs: {counter_green}')
print(f'Max eggs: {max_number} -> {color}')