soma = cont = 0

while True:
    num = int(input("Digite um número: "))

    if num == 999:
        break

    soma += num
    cont += 1

print(f"A soma entre todos os valores é {soma}.")
print(f"Foram digitados {cont} números.")
print("Acabou!")