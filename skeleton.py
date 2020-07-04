minutes_control = int(input())
seconds_control = int(input())
length = float(input())
seconds_for_hundred_meters = int(input())

control = minutes_control * 60 + seconds_control

time_of_player = length * seconds_for_hundred_meters / 100 - length * 2.5 / 120

if time_of_player <= control:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {time_of_player:.3f}.')
else:
    print(f'No, Marin failed! He was {time_of_player - control:.3f} second slower.')