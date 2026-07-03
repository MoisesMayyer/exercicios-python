preco = float(input('Digite o valor do produto: '))
form = input('Digite a forma de pagamento: ').lower()

dc = preco - (preco * 10)/100
vista = preco - (preco * 5)/100

if form in ['dinheiro', 'cheque']:
    print(f'Você pagará {dc:.2f}')

elif form == 'vista':
    print(f'Você pagará {vista:.2f}')

elif form == 'parcelado':
    x = int(input('Quantas vezes deseja parcelar? '))

    if x == 2:
        x2 = preco / 2
        print(f'Você pagará {x2:.2f} por 2 meses')

    elif x >= 3:
        x3 = preco + (preco * 20)/100
        parcela = x3 / x
        print(f'Você pagará {parcela:.2f} em {x} vezes')

    else:
        print('Parcelamento inválido')

else:
    print('Forma de pagamento inválida')
