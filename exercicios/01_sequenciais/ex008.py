# Exercício 008 - Conversão de Real para Dólar

taxa_cambio = 5.24
valor_real = float(input('Digite um valor: '))
conversao = valor_real/taxa_cambio

print(f"Com R$ {valor_real:.2f}, você pode comprar US$ {conversao:.2f}")
