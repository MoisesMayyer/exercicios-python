# Exercício 009 - Cálculo de área e tinta necessária

altura = float(input("Digite a altura em metros: "))
largura = float(input("Digite a largura em metros: "))

area = altura * largura

rendimento_tinta = 2
litros = area / rendimento_tinta

print(f"A área é {area:.2f} m² e você gastará {litros:.2f} litros de tinta")
