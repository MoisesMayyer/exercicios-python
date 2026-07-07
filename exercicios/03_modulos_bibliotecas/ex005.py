import random
a1 = str(input('digite o primeiro nome '))
a2 = str(input('digite o segundo nome '))
a3 = str(input('digite o terceiro nome '))
a4 = str(input('digite o quarto nome '))
lista = [a1,a2,a3,a4]
ordem= random.sample(lista, len(lista))
print(lista)

