# exercício 005 - listagem
import random

nome1 = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))

lista_nomes = [nome1,nome2,nome3,nome4]

ordem_lista = random.sample(lista_nomes, len(lista_nomes))

print(lista_nomes)

