name = input()
points_winner = 0

while name != "Stop":
    points_player = 0
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            points_player += 10
        else:
            points_player += 2
    if points_player >= points_winner:
        winner = name
        points_winner = points_player
    name = input()

print(f"The winner is {winner} with {points_winner} points!")