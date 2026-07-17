soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ""
mulheres_menos_20 = 0

for pessoa in range(1, 5):
    print(f"\n--- {pessoa}ª Pessoa ---")

    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().lower()

    soma_idades += idade

    if sexo == "m" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome

    if sexo == "f" and idade < 20:
        mulheres_menos_20 += 1

media_idades = soma_idades / 4

print(f"\nMédia de idade: {media_idades:.1f} anos")
print(
    f"Homem mais velho: {nome_homem_mais_velho} "
    f"({idade_homem_mais_velho} anos)"
)
print(f"Mulheres com menos de 20 anos: {mulheres_menos_20}")
