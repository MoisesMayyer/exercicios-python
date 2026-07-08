# exercício 002 - hipotenusa de um triangulo retangulo
import math

cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjascente = float(input('Digite o valor cateto adjascente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjascente)

print('sua hipotenusa é: ', hipotenusa)
