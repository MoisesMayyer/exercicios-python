soma = 0

while True:
    numero = int(input("Digite um número (999 para parar): "))

    if numero == 999:
        break

    soma += numero

print(f"A soma dos valores é {soma}.")