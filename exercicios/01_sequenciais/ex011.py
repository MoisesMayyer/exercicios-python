# Exercício 011 - Cálculo de aumento salarial

salario = float(input('digite seu salario: '))
percentual_aumento = float(input('digite o aumento (%): '))

valor_aumento= salario * (percentual_aumento / 100)

print(f"O salario ira sair de {salario:.2f} " 
      f"para {salario + valor_aumento:.2f} "  
      f"com um aumento de {valor_aumento:.2f} " 
)