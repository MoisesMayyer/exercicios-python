
for c in range (1, 6):
    f = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
    invert =(f[::-1])
    if  f == invert:
        print(f'{invert} um palindromo')
    else:
        print(f'{f} nao é palindromo')
