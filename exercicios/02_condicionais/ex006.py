n1 = int(input("Digite o primeiro: "))
n2 = int(input("Digite o segundo: "))
n3 = int(input("Digite o terceiro: "))

maior = n1

if n2 > maior:
    maior = n2

if n3 > maior:
    maior = n3

print(f'O maior é:{maior}')