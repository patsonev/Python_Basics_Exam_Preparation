count_movies = int(input())

max_rating = 0
min_rating = 11
total_rating = 0

for i in range(0, count_movies):
    movie_name = input()
    rating = float(input())
    if rating > max_rating:
        max_rating = rating
        movie_with_max = movie_name
    if rating < min_rating:
        min_rating = rating
        movie_with_min = movie_name
    total_rating += rating

avg_rating = total_rating / count_movies

print(f'{movie_with_max} is with highest rating: {max_rating:.1f}')
print(f'{movie_with_min} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {avg_rating:.1f}')
