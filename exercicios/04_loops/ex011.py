somaI = 0
maiorM = 0
nomeM = ''
maiorF = 0
nomeF = ''
idade20 = 0
for c in range(1,5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    somaI += idade
    if sexo == 'm':
        if maiorM == 0 or idade > maiorM:
            maiorM = idade
            nomeM = nome
    if sexo == 'f':
        if maiorF == 0 or idade > maiorF:
            maiorF = idade
            nomeF = nome
    if sexo == 'f' and idade < 20:
        idade20 += 1
print(f'media de: {somaI/4} ')
print(f'o homem mais velho é {nomeM} e tem {maiorM} anos')
print(f'a mulher mais veha é {nomeF} tem {maiorF} anos')
print(f'temos {idade20} mulheres com menos de 20 anos')

