numD = soma = cont = 0

while True:
    num = int(input('digite um numero'))
    if num == 999:
        break
    cont += 1
    soma += num
    print (f'a soma entre todos os valores é {soma} e temos {cont} termos')


print('cABOU')