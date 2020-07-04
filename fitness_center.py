visitors = int(input())

counter_back = 0
counter_chest = 0
counter_legs = 0
counter_abs = 0
counter_protein_shake = 0
counter_protein_bar = 0
counter_train = 0
counter_buy = 0

for i in range(0, visitors):
    acts = input()
    if acts == 'Back':
        counter_back += 1
        counter_train += 1
    elif acts == 'Chest':
        counter_chest += 1
        counter_train += 1
    elif acts == 'Legs':
        counter_legs += 1
        counter_train += 1
    elif acts == 'Abs':
        counter_abs += 1
        counter_train += 1
    elif acts == 'Protein shake':
        counter_protein_shake += 1
        counter_buy += 1
    elif acts == 'Protein bar':
        counter_protein_bar += 1
        counter_buy += 1

print(f'{counter_back} - back')
print(f'{counter_chest} - chest')
print(f'{counter_legs} - legs')
print(f'{counter_abs} - abs')
print(f'{counter_protein_shake} - protein shake')
print(f'{counter_protein_bar} - protein bar')
print(f'{counter_train * 100 / visitors:.2f}% - work out')
print(f'{counter_buy * 100 / visitors:.2f}% - protein')