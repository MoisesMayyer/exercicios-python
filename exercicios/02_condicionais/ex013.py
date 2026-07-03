ano = int(input('qual o ano de nascimento: '))
idade = 2026 -ano
if idade <= 9:
    print(f'{idade} atleta mirim')
elif  9 < idade <= 14:
    print (f'{idade} atleta infantil')
elif 14 < idade < 19:
    print(f'{idade} atleta junior')
elif 19 < idade < 20 :
    print(f'{idade} atleta senior')
else:
    print(f'{idade} atleta master')
