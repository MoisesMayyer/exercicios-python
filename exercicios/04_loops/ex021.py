import random

while True:
    comput = random.randint(0, 10)  # agora muda sempre

    pi = str(input('Par ou ímpar? ')).strip().lower()
    player = int(input('Digite sua jogada: '))

    jogo = player + comput

    if jogo % 2 == 0:
        resultado = 'par'
    else:
        resultado = 'impar'

    print(f'Você jogou {player} e o computador {comput}. Total = {jogo} ({resultado})')

    if pi == resultado:
        print('Você venceu! ')
    else:
        print('Computador venceu! ')
        break
