max_points = 0

for i in range(0, 7):
    movie_name = input()
    total_points = 0
    if movie_name == 'STOP':
        break
    length_movie_name = len(movie_name)
    for j in range(0, length_movie_name):
        points = int(ord(movie_name[j]))
        total_points += points
        if movie_name[j] != ' ' and not movie_name[j].isdigit():
            if movie_name[j].islower():
                total_points -= 2 * length_movie_name
            else:
                total_points -= length_movie_name
    if total_points > max_points:
        max_points = total_points
        name_max_points = movie_name
    if i == 6:
        print(f'The limit is reached.')
        break

print(f'The best movie for you is {name_max_points} with {max_points} ASCII sum.')
