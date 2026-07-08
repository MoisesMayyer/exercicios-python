t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
n = int(input('Digite a quantidade de termos: '))
c = 1
while c != n:
    c += 1
    pa = t1 + (c - 1 )*r
    print(pa)