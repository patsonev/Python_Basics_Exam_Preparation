total_seats = int(input())
command = input()

total_income = 0
people_at_hall = 0
count_people = 0

while command != 'Movie time!':
    count_people = int(command)
    people_at_hall += count_people
    if people_at_hall > total_seats:
        print(f'The cinema is full.')
        break
    money = count_people * 5
    if count_people % 3 == 0:
        money -= 5
    total_income += money
    command = input()

if command == 'Movie time!':
    print(f'There are {total_seats - people_at_hall} seats left in the cinema.')

print(f'Cinema income - {total_income} lv.')