peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))
imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print('Abaixo do peso')

elif 18.5 <= imc <= 25:
    print('peso ideal')

elif 25 < imc <= 30:
    print('Sobrepeso')

elif 30 < imc <= 40:
    print('Obesidade')

else:
    print('obesidade morbida')
