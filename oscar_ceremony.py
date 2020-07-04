price_hall = int(input())

price_state = 0.7 * price_hall
price_ketyring = price_state * 0.85
price_sound = price_ketyring / 2

print(f'{price_ketyring + price_state + price_hall + price_sound:.2f}')