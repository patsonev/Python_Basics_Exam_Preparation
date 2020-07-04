goal_high = int(input())

current_jump = 0
current_goal = goal_high - 30
counter_total = 0
counter_unsuccessful = 0

while current_goal <= goal_high:
    current_jump = int(input())
    counter_total += 1
    if current_jump > current_goal:
        current_goal += 5
        counter_unsuccessful = 0
    else:
        counter_unsuccessful += 1
    if counter_unsuccessful == 3:
        print(f'Tihomir failed at {current_goal}cm after {counter_total} jumps.')
        break

if current_goal > goal_high:
    print(f'Tihomir succeeded, he jumped over {goal_high}cm after {counter_total} jumps.')