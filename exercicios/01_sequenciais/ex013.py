km=float(input('digite a quatidade percorrida em km'))
dias=int(input('digite a quantidade de dias'))
calcD= 60 * dias
calcK= 0.15 * km
print('os valores a serem pagos sao: {} por dias alugados e {} por km rodados'.format(calcD,calcK))
print('valor total =',(calcK + calcD),'reais')
