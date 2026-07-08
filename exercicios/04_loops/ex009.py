
t1 = 0
t2 = 0

for c in range (1, 8):
    p = int(input('digite o seu ano de nascimento'))
    idade = 2026 - p
    if idade >= 21:
        t1 += 1
    else:
        t2 += 1
print(f'{t1} pessoas maiores de 20 anos e {t2} pessoas menores de 20 anos')