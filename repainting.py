kolichestvo_nailon = int(input())
kolichestvo_boq = int(input())
kolichestvo_razreditel = int(input())
chasove = int(input())

cena_nailon = (kolichestvo_nailon + 2) * 1.5
cena_boq = kolichestvo_boq * 1.1 * 14.5
cena_razreditel = kolichestvo_razreditel * 5
cena_rabota = chasove * 0.3 * (cena_boq + cena_nailon + cena_razreditel + 0.4)

obshto_cena = cena_razreditel + cena_nailon + cena_boq + cena_rabota + 0.4

print(f'Total expenses: {obshto_cena:.2f} lv.')