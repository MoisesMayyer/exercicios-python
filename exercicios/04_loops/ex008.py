#exercício 008 - verificação de palíndromo

for _ in range(1, 6):
    frase = input("Digite uma frase: ").strip().lower().replace(" ", "")
    frase_invertida = frase[::-1]

    if frase == frase_invertida:
        print(f"{frase_invertida} é um palíndromo")
    else:
        print(f"{frase} não é um palíndromo")