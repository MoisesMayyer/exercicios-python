# Exercício 010 - Cálculo de desconto em um produto

produto = float(input("Digite o valor do produto: "))
percentual_desconto = float(input("Digite o desconto (%): ").replace("%", ""))

desconto = produto * (percentual_desconto / 100)
preco_final = produto - desconto

print(
    f"O valor do produto é R$ {produto:.2f}, "
    f"o desconto é de R$ {desconto:.2f} "
    f"e o preço final é R$ {preco_final:.2f}"
)