# Exercício 6 - verificação de numero maior entre 3 numeros

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior_numero = numero1

if numero2 > maior_numero:
    maior_numero = numero2

if numero3 > maior_numero:
    maior_numero = numero3

print(f"O maior número é: {maior_numero}")