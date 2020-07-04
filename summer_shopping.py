budget = int(input())
price_havliq = float(input())
discount = int(input())

price_umbrella = 2 * price_havliq / 3
price_djapanki = 0.75 * price_umbrella
price_chanta = (price_djapanki + price_havliq) / 3

total_price = (price_havliq + price_djapanki + price_umbrella + price_chanta) * (1 - discount / 100)

if total_price <= budget:
    print(f"Annie's sum is {total_price:.2f} lv. She has {budget - total_price:.2f} lv. left.")
else:
    print(f"Annie's sum is {total_price:.2f} lv. She needs {total_price - budget:.2f} lv. more.")