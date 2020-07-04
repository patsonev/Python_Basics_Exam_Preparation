count_eggs = int(input())

command = ' '
sold_eggs = 0

while command != 'Close':
    command = input()
    if command == 'Buy':
        eggs = int(input())
        sold_eggs += eggs
        count_eggs -= eggs
        if count_eggs < 0:
            print(f'Not enough eggs in store!\nYou can buy only {count_eggs + eggs}.')
            break
    elif command == 'Fill':
        eggs = int(input())
        count_eggs += eggs
    elif command == 'Close':
        print(f'Store is closed!\n{sold_eggs} eggs sold.')