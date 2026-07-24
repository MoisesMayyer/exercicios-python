import math

continuar = "s"

while continuar.lower() != "n":
    numero = int(input("Digite um número: "))
    print(f"Fatorial: {math.factorial(numero)}")

    continuar = input("Deseja continuar? [S/N]: ")