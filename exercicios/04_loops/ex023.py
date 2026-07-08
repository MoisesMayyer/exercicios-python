tot = 0
item = 0
menor_preco = 0
nomemenor = ''
cont = 0
while True:
    cont += 1
    print('loja do mayer')
    nome = str(input('digite o nome do porduto: '))
    preco = int(input('digite o valor do produto: '))
    tot += preco
    if preco >= 1000:
        item += 1
    if cont == 1:
        menor_preco = preco
        nomemenor = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            nomemenor = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print(f'o valor toal em compras foi de {tot}')
print(f'tem {item} que custam mais de 1000 reais')
print(f'o produto mais barato é {nomemenor} custando {menor_preco} reais')
