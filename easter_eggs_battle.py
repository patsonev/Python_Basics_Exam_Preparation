eggs_first = int(input())
eggs_second = int(input())
command = ' '

while eggs_first != 0 and eggs_second != 0:
    command = input()
    if command == 'End of battle':
        print(f'Player one has {eggs_first} eggs left.')
        print(f'Player two has {eggs_second} eggs left.')
        break
    if command == 'one':
        eggs_second -= 1
    elif command == 'two':
        eggs_first -= 1

if eggs_first == 0:
    print(f"Player one is out of eggs. Player two has {eggs_second} eggs left.")
elif eggs_second == 0:
    print(f"Player two is out of eggs. Player one has {eggs_first} eggs left.")