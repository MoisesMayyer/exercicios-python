# exercício 013 - classificação de atletas

from datetime import date

ano_nascimento = int(input('Qual o ano de nascimento: '))

ano_atual = date.today().year
idade_atleta = ano_atual - ano_nascimento

if idade_atleta <= 9:
    print(f'{idade_atleta} anos - Atleta Mirim')
elif idade_atleta <= 14:
    print(f'{idade_atleta} anos - Atleta Infantil')
elif idade_atleta <= 19:
    print(f'{idade_atleta} anos - Atleta Júnior')
elif idade_atleta <= 20:
    print(f'{idade_atleta} anos - Atleta Sênior')
else:
    print(f'{idade_atleta} anos - Atleta Master')