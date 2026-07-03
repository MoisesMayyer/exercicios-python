import random

num = random.choice(['pedra', 'papel', 'tesoura'])
print('vamos jogar jokempo')

player = input('1...2...3....vai! ').lower().strip()

if player not in ['pedra', 'papel', 'tesoura']:
    print('jogada invalida')

elif player == num:
    print('empate')
    print(num)

elif (
    (player == 'pedra' and num == 'tesoura') or
    (player == 'papel' and num == 'pedra') or
    (player == 'tesoura' and num == 'papel')
):
    print('voce ganhou')
    print(num)

else:
    print('voce perdeu')
    print(num)