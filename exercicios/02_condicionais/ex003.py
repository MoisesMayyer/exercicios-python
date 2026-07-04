# exercicios 03 - verifica se o numero é par ou impar

numero_escolhido = int(input('Digite um numero aleatorio: '))

mensagem = (
    f'O numero {numero_escolhido} é par' if numero_escolhido % 2 == 0 else f'O numero {numero_escolhido} é impar')

print(mensagem)