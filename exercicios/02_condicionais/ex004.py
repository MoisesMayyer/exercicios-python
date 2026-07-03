km =float(input('qual a distancia da viagem: '))
if km<=200:
    print(f'para essa viagem vc gastara {0.50*km} de passagem')
else:
    print(f'como essa viagem é mais longa vc pagara {0.45* km} de passagem')