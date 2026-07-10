# exercício 004 - Tabuada de um número escolhido pelo usuário
from time import sleep 

tabuada = int(input('Escolha o numero da sua tabuada:'))

for contador in range (1,11):
    sleep(0.5)
    print(f'{tabuada} X {contador} = {tabuada * contador}')