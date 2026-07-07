# exercício 009 - financiamento de uma casa

valor_casa = float(input('Digite o valor da casa: '))
anos_financiamento = int(input('Digite em quantos anos deseja pagar: '))
salario = float(input('Digite seu salario: '))

limite_parcela = salario * 0.30
quantidade_parcelas = (anos_financiamento * 12)
valor_parcela = valor_casa / quantidade_parcelas

print(f'Valor da parcela: R$ {valor_parcela:.2f}')
print(f'Limite da parcela: R$ {limite_parcela:.2f}')

if valor_parcela > limite_parcela:
    print("Infelizmente você não poderá comprar esta casa com seu salário.")
else:
    print("Você poderá comprar esta casa.")

