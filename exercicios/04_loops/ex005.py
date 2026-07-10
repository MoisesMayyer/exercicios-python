#exercício 005 - soma de números pares

soma_pares = 0

for contador in range (1,7):

    numero = int(input(f'Digite o {contador}º numero: '))

    if numero % 2 == 0:
        soma_pares += numero

print(f'S soma dos numeros pares foi: {soma_pares}')        