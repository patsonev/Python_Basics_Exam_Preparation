name_actor = input()
points_from_academy = float(input())
count_commission = int(input())

total_points = 0

for i in range(0, count_commission):
    name = input()
    points = float(input()) * len(name) / 2
    points_from_academy += points
    if points_from_academy > 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academy:.1f}!")
        break

if points_from_academy <= 1250.5:
    print(f'Sorry, {name_actor} you need {1250.5 - points_from_academy:.1f} more!')