import random
num = random.choice(('Pedra', 'Papel', 'Tesoura')).strip().lower()
print('vamos jogar jokempo')
player= str(input('1...2...3....vai!')).lower().strip()

if player not in ['pedra', 'papel', 'tesoura']:
    print('jogada invalida')

elif player == 'pedra' and num == 'papel':
    print('voce perdeu')
    print(num)
elif player == 'pedra' and num == 'tesoura':
    print('voce ganhou')
    print(num)

elif player == 'papel' and num == 'tesoura':
    print('voce perdeu')
    print(num)
elif player == 'papel' and num == 'pedra':
    print('voce ganhou')
    print(num)

elif player == 'tesoura' and num == 'pedra':
    print('voce perdeu')
    print(num)
elif player == 'tesoura' and num == 'papel':
    print('voce ganhou')
    print(num)
else:
    print('empate')
    print(num)