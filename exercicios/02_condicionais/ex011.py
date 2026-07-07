# exercício 011 - alistamento militar

ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade = 2026 - ano_nascimento
idade_alistamento = idade - 18

if idade == 18:
    print('Você deve se alistar imediatamente.')
elif idade < 18:
    print(f'Você ainda não pode se alistar. Faltam {18 - idade} anos para o alistamento.')
else:
    print(f'Já se passaram {idade_alistamento} anos desde o alistamento.')