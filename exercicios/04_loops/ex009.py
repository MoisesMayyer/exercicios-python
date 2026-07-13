#exercício 009 - verificação de idade

maiores_idade = 0
menores_idade = 0

for _ in range(7):
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    idade = 2026 - ano_nascimento

    if idade >= 21:
        maiores_idade += 1
    else:
        menores_idade += 1

print(
    f"{maiores_idade} pessoas maiores de 20 anos e "
    f"{menores_idade} pessoas menores de 20 anos."
)