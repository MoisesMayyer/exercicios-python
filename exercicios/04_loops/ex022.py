maiores_18 = 0
homens = 0
mulheres_menores_20 = 0

while True:
    print("=" * 10 + " Cadastre uma pessoa " + "=" * 10)

    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()

    if sexo == "M":
        homens += 1

    if idade > 18:
        maiores_18 += 1

    if sexo == "F" and idade < 20:
        mulheres_menores_20 += 1

    continuar = input("Quer continuar? [S/N]: ").strip().upper()

    if continuar == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {maiores_18}")
print(f"Total de homens: {homens}")
print(f"Total de mulheres com menos de 20 anos: {mulheres_menores_20}")