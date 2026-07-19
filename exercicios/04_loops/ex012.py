while True:
    sexo = input('Digite seu sexo [M/F]: ').strip().upper()

    if sexo in ('M', 'F'):
        print('Sexo cadastrado com sucesso!')
        break

    continuar = input(
        f'"{sexo}" não é uma opção válida. Deseja tentar novamente? [S/N]: '
    ).strip().upper()

    if continuar == 'N':
        breakS

