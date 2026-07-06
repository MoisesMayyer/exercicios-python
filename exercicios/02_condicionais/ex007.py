# exercício 007 - Aumentos múltiplos

salario_atual = float(input('Qual o seu salario: '))

if salario_atual > 1250:
    aumento = 0.10
else:
    aumento = 0.15

novo_salario = salario_atual * (1 + aumento)

print(f"Seu salário passará a ser R$ {novo_salario:.2f}")