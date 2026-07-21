import random

numero_secreto = random.randint(1, 10)
tentativas = 0

print("Vamos jogar um jogo de adivinhar o número de 1 a 10!")
print("=" * 40)
print("Tente descobrir o número que eu escolhi.")
print("=" * 40)

# Apenas para testes
# print(numero_secreto)

while True:
    palpite = int(input("Digite um número: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"\nParabéns! Você acertou.")
        print(f"O número era {numero_secreto}.")
        print(f"Você precisou de {tentativas} tentativa(s).")
        break

    print("Você errou. Tente novamente!\n")
