import random
c = 1
erros = 0
numA = random.randint(1, 10)

print('Vamos jogar um jogo de advinhar o numero de 0 a 10!!!')
print('===='*10)
print ('tente advinhar o numero que escolhi')
print('==='*10)
print(numA)
while c != 0:
    resp =int(input('digite um valor: '))
    if resp == numA:

        print(f'Voce acertou o numero era {numA}')
        print(f'voce levou {erros} tentativas')
        break
    else:
        print('continue tentando acertar !!')
        erros += 1

