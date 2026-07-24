import random

while True:
    computador = random.randint(0, 10)

    escolha = input("Par ou ímpar? ").strip().lower()
    jogador = int(input("Digite sua jogada: "))

    total = jogador + computador

    resultado = "par" if total % 2 == 0 else "impar"

    print(f"\nVocê jogou {jogador} e o computador {computador}.")
    print(f"Total: {total} ({resultado})")

    if escolha == resultado:
        print("Você venceu!")
    else:
        print("Computador venceu!")
        break