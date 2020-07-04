time = int(input())
count_scenes = int(input())
time_per_scene = int(input())

needed_time = count_scenes * time_per_scene + 0.15 * time

if needed_time <= time:
    print(f'You managed to finish the movie on time! You have {round(time - needed_time)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(needed_time - time)} minutes.')