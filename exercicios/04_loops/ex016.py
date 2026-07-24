primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
quantidade = int(input("Digite a quantidade de termos: "))

contador = 0

while contador < quantidade:
    termo = primeiro_termo + contador * razao
    print(termo)
    contador += 1