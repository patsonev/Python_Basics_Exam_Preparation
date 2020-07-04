import math

name = input()
length_episode = int(input())
length_rest = int(input())

if length_episode > 5 * length_rest / 8:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(length_episode - 5 * length_rest / 8)} more minutes.")
else:
    print(f'You have enough time to watch {name} and left with {math.ceil(5 * length_rest / 8 - length_episode)} minutes free time.')