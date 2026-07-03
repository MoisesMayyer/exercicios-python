ano = int(input('Qual o ano do seu nascimento? '))
idade = 2026 - ano
ia = idade - 18
if idade == 18:
    print('bota irmao se alistar ')
elif idade < 18:
    print(f'ainda vai chegar sua hora de se alistar, falta {ia} anos para se alistar')
else:
    print(f'ja passou o tempo de se alistar. passou {ia} anos de se alistar')