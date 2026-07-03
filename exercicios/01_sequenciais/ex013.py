# Exercício 013 - Cálculo do valor a pagar por um carro alugado

km = float(input("Digite a quantidade percorrida em km: "))
quantidade_dias = int(input("Digite a quantidade de dias: "))

valor_dias = 60 * quantidade_dias
valor_km = 0.15 * km

total = valor_dias + valor_km

print(
    f"Valor pelos dias alugados: R$ {valor_dias:.2f}\n"
    f"Valor pelos km rodados: R$ {valor_km:.2f}\n"
    f"Total a pagar: R$ {total:.2f}"
)