salario = float(input('Qual o seu salario: '))
if salario > 1250:
    print(f'seu salario passara a ser {((salario*10)/100) + salario}')
else:
    print(f'seu saliro passara a ser {((salario * 15)/100) + salario}')