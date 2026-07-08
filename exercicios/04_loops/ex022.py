id18 = 0
h = 0
m20 = 0



while True:
    print('='*10 + 'cadastre uma pessoa' + '='*10)
    idade = int(input('Idade: '))
    sexo = str(input('sexo: [M/F]')).upper().strip()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()
    if sexo == 'M':
        h += 1
    if idade > 18:
        id18 += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    if resp == 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {id18}')
print(f'total de homens foi de {h}')
print(f'total de mulheres com menos de 20 anos: {m20}')