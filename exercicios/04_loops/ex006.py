t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
n = int(input('Digite a quantidade de termos: '))
for c in range(1,n + 1):
    pa = t1 + (c - 1 )*r
    print(pa)