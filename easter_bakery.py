cena_brashno = float(input())
kg_brashno = float(input())
kg_zahar = float(input())
broi_kori_qica = int(input())
paketi_maq = int(input())

cena_zahar = cena_brashno * 0.75
cena_kora_qica = cena_brashno * 1.1
cena_maq = cena_zahar * 0.2

suma_cena = kg_brashno * cena_brashno + kg_zahar * cena_zahar + broi_kori_qica * cena_kora_qica + paketi_maq * cena_maq
print(f'{suma_cena:.2f}')