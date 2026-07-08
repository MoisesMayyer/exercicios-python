# exercício 004 - sorteio de um aluno

import random
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))

aluno_escolhido = random.choice([aluno1, aluno2, aluno3, aluno4])

print(f'o aluno sorteado foi: {aluno_escolhido}')
