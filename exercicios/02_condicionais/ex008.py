r1 =float(input('digite a primeria reta'))
r2 =float(input('digite a segunda reta'))
r3 =float(input('digite a terceira reta'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('forma um triangulo')
else:
    print('nao forma um triangulo')