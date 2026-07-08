cont = 'S'
while cont != 'N':
    sex = str(input('digite seu sexo [M/F]')).strip().upper()
    if sex != 'M' and sex != 'F':
        cont= str(input(f'{sex} nn foi aceito. deseja tentar novamente [S/N]')).upper()

