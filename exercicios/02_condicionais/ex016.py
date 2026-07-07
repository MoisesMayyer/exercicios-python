# exercício 016 - jogo de pedra, papel e tesoura
import random

opcoes = ['pedra', 'papel', 'tesoura']

jogada_computador = random.choice(opcoes)

print('Vamos jogar joquempô!')

jogada_jogador = input('1... 2... 3... vai! ').lower().strip()

if jogada_jogador not in opcoes:
    print('Jogada inválida.')

elif jogada_jogador == jogada_computador:
    print('Empate!')

elif (
    (jogada_jogador == 'pedra' and jogada_computador == 'tesoura') or
    (jogada_jogador == 'papel' and jogada_computador == 'pedra') or
    (jogada_jogador == 'tesoura' and jogada_computador == 'papel')
):
    print('Você ganhou!')

else:
    print('Você perdeu!')

print(f'O computador escolheu {jogada_computador}.')