valor =float(input('digite o valor da casa'))
ano= int(input('digite em quantos anos deseja pagar'))
sal= float(input('digite seu salario'))
m = (sal*30)/100
p = (ano*12)
prest = valor / p
if  prest > m :
    print(f'infelizmente vc nao podera comprar esta casa com seu salario')
else:
    print(f'voce podera comprar esta casa')