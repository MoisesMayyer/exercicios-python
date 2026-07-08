a1 = int(input('Digite o primeiro valor: '))
a2 = int(input('Digite o segundo valor: '))
resp = 0
menu = str("""[1]somar
[2] multiplicar
[3] dividir
[4] novos numeros
[5] sair do programa
""")
while resp != 5:
    print(menu)
    resp = int(input('qual a opcao: '))

    if resp == 1:
        soma = a1 + a2
        print(f'a soma entre {a1} + {a2} = {soma}')


    elif resp == 2:
        multiplicar = a1 * a2
        print(f'a multiplicação entre {a1} * {a2} = {multiplicar}')


    elif resp == 3:
        dividir = a1 / a2
        print(f'a divisao entre {a1} e {a2} é {dividir}')
    elif resp == 4:
        a1 = int(input('informe o primeiro valor: '))
        a2 = int(input('informe o segundo valor: '))




