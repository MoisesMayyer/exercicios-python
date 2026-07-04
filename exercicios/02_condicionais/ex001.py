# exercício 1 - adivinhação de numero

import random

numero_misterioso = random.randint(0, 5)

print('Tente acertar o numero misterioso')


numero_escolhido = int(input('digite um numero de 0 a 5: '))

mensagem = (
    f'Parabéns, você acertou! O número era {numero_misterioso}.'
    if numero_misterioso == numero_escolhido
    else 'Que ruim, tente novamente.'
)

print(mensagem)