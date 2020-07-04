money_food_day = float(input())
money_souvenirs_day = float(input())
money_hotel_day = float(input())

money_travel = 420 / 100 * 7 * 1.85
money_food = 3 * money_food_day
money_souvenirs = 3 * money_souvenirs_day
money_hotel = money_hotel_day * (0.9 + 0.85 + 0.8)

total_money = money_hotel + money_souvenirs + money_food + money_travel

print(f'Money needed: {total_money:.2f}')