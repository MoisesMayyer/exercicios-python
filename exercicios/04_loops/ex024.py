soma = 0
pares = 0
impares = 0
quantidade = 0
maior_numero = 0

while True:
    numero = int(input("Digite um valor [0 para parar]: "))

    if numero == 0:
        break

    soma += numero
    quantidade += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if quantidade == 1 or numero > maior_numero:
        maior_numero = numero

print(f"Total de números digitados: {quantidade}")
print(f"Total de números pares: {pares}")
print(f"Total de números ímpares: {impares}")
print(f"A soma de todos foi: {soma}")
print(f"O maior número digitado foi: {maior_numero}")