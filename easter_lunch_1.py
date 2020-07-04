kozunaci = int(input())
kori_qica = int(input())
kurabii = int(input())

cena_kozunaci = kozunaci * 3.2
cena_kori_qica = kori_qica * 4.35
cena_kurabii = kurabii * 5.4
cena_boq = kori_qica * 12 * 0.15

suma_cena = cena_boq + cena_kori_qica + cena_kozunaci + cena_kurabii
print(f'{suma_cena:.2f}')