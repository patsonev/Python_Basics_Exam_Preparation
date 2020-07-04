import math

command = " "
max_points = 0
glasni = "eyuioaEYUIOA"

while command != 'End of words':
    points = 0
    for i in range(len(command)):
        current_points = ord(command[i])
        points += current_points
    if str(command[0]) in glasni:
        points = points * len(command)
    else:
        points = math.floor(points / len(command))
    if points > max_points:
        max_points = points
        winner = command
    command = input()

print(f"The most powerful word is {winner} - {max_points}")
