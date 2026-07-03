#oq caralhos é um ano bissexto
ano=int(input('digite o ano em que voce esta'))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'o ano de {ano} é bissexto')
else:
    print(f'o ano de {ano} nao é bissexto')
