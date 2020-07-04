movie_name = input()
count_days = int(input())
count_tickets = int(input())
price_ticket = float(input())
percent_for_cinema = int(input())

profit = count_days * count_tickets * price_ticket * (100 - percent_for_cinema) / 100

print(f'The profit from the movie {movie_name} is {profit:.2f} lv.')