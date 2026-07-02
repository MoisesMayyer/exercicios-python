produto=float(input('digite o valor do produto'))
desconto= (produto*5)/100
Pfinal= produto - desconto
print('voce tera `{:.2f} de desconto e o valor final ficara {}'.format(desconto, Pfinal))