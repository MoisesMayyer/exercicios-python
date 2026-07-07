import random
aluno1 = str(input('digite o nome do primeiro aluno'))
aluno2 = str(input('digite o nome do segundo aluno'))
aluno3 =str(input('digite o numero do terceiro aluno'))
aluno4 = str(input('digite o nome do quarto aluno'))
escolha = random.choice([aluno1,aluno2,aluno4])
print('o aluno sorteado foi {}'.format(escolha))
