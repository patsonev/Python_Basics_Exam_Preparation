movie_name = input()
kind_hall = input()
count_tickets = int(input())

if kind_hall == 'normal':
    if movie_name == 'A Star Is Born':
        price = 7.5
    elif movie_name == 'Bohemian Rhapsody':
        price = 7.35
    elif movie_name == 'Green Book':
        price = 8.15
    elif movie_name == 'The Favourite':
        price = 8.75

elif kind_hall == 'luxury':
    if movie_name == 'A Star Is Born':
        price = 10.5
    elif movie_name == 'Bohemian Rhapsody':
        price = 9.45
    elif movie_name == 'Green Book':
        price = 10.25
    elif movie_name == 'The Favourite':
        price = 11.55

elif kind_hall == 'ultra luxury':
    if movie_name == 'A Star Is Born':
        price = 13.5
    elif movie_name == 'Bohemian Rhapsody':
        price = 12.75
    elif movie_name == 'Green Book':
        price = 13.25
    elif movie_name == 'The Favourite':
        price = 13.95

print(f'{movie_name} -> {price * count_tickets:.2f} lv.')