total = 0
quantidade_mil = 0
menor_preco = 0
nome_menor = ""

contador = 0

while True:
    print("Loja do Mayer")

    nome = input("Digite o nome do produto: ")
    preco = int(input("Digite o valor do produto: "))

    contador += 1
    total += preco

    if preco >= 1000:
        quantidade_mil += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        nome_menor = nome

    resposta = ""

    while resposta not in "SN":
        resposta = input("Quer continuar? [S/N]: ").strip().upper()[0]

    if resposta == "N":
        break

print(f"O valor total das compras foi de R${total}")
print(f"Tem {quantidade_mil} produtos custando mais de R$1000")
print(f"O produto mais barato é {nome_menor}, custando R${menor_preco}")