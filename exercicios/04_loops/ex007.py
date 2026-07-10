# exercício 007 - Maior número digitado
maior_numero = None

for c in range(1, 11):
    numero = int(input(f'Digite o {c}º numero: '))

    if c == 1:
        maior_numero = numero
    elif numero > maior_numero:
        maior_numero = numero

print(f'O maior numero digitado foi {maior_numero}')
    