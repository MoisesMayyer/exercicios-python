#exercício 010 - calculo de peso

maior_peso = 0
menor_peso = 0

for pessoa in range(1, 6):
    peso = float(input(f"Digite o peso da {pessoa}ª pessoa: "))

    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
        continue

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f"\nMaior peso: {maior_peso:.1f} kg")
print(f"Menor peso: {menor_peso:.1f} kg")