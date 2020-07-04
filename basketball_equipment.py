year_tax = int(input())

shoes_price = 0.6 * year_tax
dresses_price = shoes_price * 0.8
ball_price = 0.25 * dresses_price
accessories_price = 0.2 * ball_price

print(f'{year_tax + shoes_price + dresses_price + ball_price + accessories_price:.2f}')