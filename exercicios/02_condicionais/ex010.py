# exercício 010 - verificação de maior e menor valor

valor1 = int(input('digite um valor: '))
valor2 = int(input('digite outro valor: '))

if valor1 > valor2:
    print(f'O maior valor é {valor1}.')
elif valor2 > valor1:
    print(f'O maior valor é {valor2}.')
else:
    print('Os dois valores são iguais.')