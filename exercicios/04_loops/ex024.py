soma = 0
par = 0
impar = 0
cont = 0
num1 = 1
maiornum = 0
while num1 != 0:

    num1 = int(input('digite um valor [0] PARA PARAR '))
    if num1 == 0:
        break
    soma += num1
    if num1 %2 == 0:
        par +=1

    else:
        impar += 1

    cont += 1
    if cont == 1:
        maiornum = num1

    else:
        if num1 > maiornum:
            maiornum = num1
print(f'total de numeros digitados {cont}')
print(f'total de numeros par {par}')
print(f'total de numeros impar {impar}')
print(f'a soma de todos foi de {soma}')
print(f'o maior numero digitado é {maiornum}')