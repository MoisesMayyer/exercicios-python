# exercício 003 - Mostrar todos os números ímpares de 1 a 500 e somar os que são múltiplos de 3

soma = 0
for numero in range (1,501, 2):
    
    if numero % 3 == 0 :
        print(numero)
        soma += numero

print(f'a soma total foi de {soma}')
