# exercício 008 - verificação de um triangulo

lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

forma_triangulo = (
    lado1 + lado2 > lado3
    and lado1 + lado3 > lado2
    and lado2 + lado3 > lado1
)

if forma_triangulo:
    print('Forma um triângulo.')
else:
    print('Não forma um triângulo.')