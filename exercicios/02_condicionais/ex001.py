import random
escolhido = random.randint(1, 5)
print('tente acertar o numero misterioso')
print(escolhido)
resp= int(input('digite um numero de 0 a 5: '))
if escolhido == resp:
   print(f'parabens voce acertou o numero era {escolhido}')
else:
    print('que ruim, tente novamente')

