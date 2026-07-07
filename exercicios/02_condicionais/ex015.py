# exercício 015 - cálculo de preço com desconto e parcelamento

preco = float(input('Digite o valor do produto: '))
forma_pagamento = input('Digite a forma de pagamento: ').lower()

desconto_dinheiro = preco * 0.90
desconto_vista = preco * 0.95

if forma_pagamento in ['dinheiro', 'cheque']:
    print(f'Você pagará R$ {desconto_dinheiro:.2f}')

elif forma_pagamento == 'vista':
    print(f'Você pagará R$ {desconto_vista:.2f}')

elif forma_pagamento == 'parcelado':
    quantidade_parcelas = int(input('Quantas vezes deseja parcelar? '))

    if quantidade_parcelas == 2:
        valor_parcela = preco / quantidade_parcelas
        print(f'Você pagará R$ {valor_parcela:.2f} em {quantidade_parcelas} vezes')

    elif quantidade_parcelas >= 3:
        preco_com_juros = preco * 1.20
        valor_parcela = preco_com_juros / quantidade_parcelas

        print(f'Você pagará R$ {valor_parcela:.2f} em {quantidade_parcelas} vezes')

    else:
        print('Parcelamento inválido.')

else:
    print('Forma de pagamento inválida.')
