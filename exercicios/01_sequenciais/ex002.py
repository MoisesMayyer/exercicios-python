# Exercício sobre análise de strings

frase = input("Digite uma frase: ")

print(f"Só letras maiúsculas: {frase.isupper()}")
print(f"Só números: {frase.isnumeric()}")
print(f"Só letras: {frase.isalpha()}")
print(f"Letras e números: {frase.isalnum()}")