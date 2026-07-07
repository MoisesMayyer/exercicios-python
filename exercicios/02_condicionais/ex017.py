# exercício 017 - jogo de pedra, papel e tesoura com computador
import random

opcoes = ('pedra', 'papel', 'tesoura')

jogada_computador = random.choice(opcoes)

print('Vamos jogar joquempô')

jogada_jogador = input('1...2...3...vai! ').lower().strip()

if jogada_jogador not in opcoes:
    print('Jogada inválida')

elif jogada_jogador == 'pedra' and jogada_computador == 'papel':
    print('Você perdeu')
    print(jogada_computador)

elif jogada_jogador == 'pedra' and jogada_computador == 'tesoura':
    print('Você ganhou')
    print(jogada_computador)

elif jogada_jogador == 'papel' and jogada_computador == 'tesoura':
    print('Você perdeu')
    print(jogada_computador)

elif jogada_jogador == 'papel' and jogada_computador == 'pedra':
    print('Você ganhou')
    print(jogada_computador)

elif jogada_jogador == 'tesoura' and jogada_computador == 'pedra':
    print('Você perdeu')
    print(jogada_computador)

elif jogada_jogador == 'tesoura' and jogada_computador == 'papel':
    print('Você ganhou')
    print(jogada_computador)

else:
    print('Empate')
    print(jogada_computador)