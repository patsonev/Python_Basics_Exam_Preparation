name = input()

count_seasons = int(input())
count_episodes = int(input())
length = float(input())

total_time = (length + 0.2 * length) * count_episodes * count_seasons + count_seasons * 10

print(f'Total time needed to watch the {name} series is {int(total_time)} minutes.')