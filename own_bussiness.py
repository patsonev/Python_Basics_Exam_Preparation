width = int(input())
length = int(input())
high = int(input())

free_space = width * length * high

while free_space > 0:
    command = input()
    if command == "Done":
        print(f'{free_space} Cubic meters left.')
        break
    else:
        count_computers = int(command)
        free_space -= count_computers

if free_space <= 0:
    print(f'No more free space! You need {abs(free_space)} Cubic meters more.')