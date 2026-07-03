vel= float(input('qual a velocida atual do carro: '))
if vel > 80:
    print(f'ta doidao maluco andando a {vel} na pista')
    print(f'sua multa sera de {(vel-80)*7}')
else:
    print(f'andando a {vel} ta dboa por enquanto...')