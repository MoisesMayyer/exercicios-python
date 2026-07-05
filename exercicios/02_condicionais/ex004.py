# exercício 4 - Calculo de distância de viagem

distancia_viagem = float(input("Qual a distância da viagem (km)? "))

if distancia_viagem <= 200:
    valor_passagem = distancia_viagem * 0.50
    print(f"Para essa viagem, você gastará R$ {valor_passagem:.2f} de passagem.")
else:
    valor_passagem = distancia_viagem * 0.45
    print(f"Como essa viagem é mais longa, você pagará R$ {valor_passagem:.2f} de passagem.")