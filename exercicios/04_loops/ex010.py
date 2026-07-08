maior = 0
menor = 0
for c in range (1,6):
    p = float(input('digite seu peso: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'o maior peso é {maior} e o menor é {menor}')
