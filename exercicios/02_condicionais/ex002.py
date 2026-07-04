# exercicios 02 - multa por velocidade

velocidade_atual = float(input('qual a velocidade atual do carro: '))

limite_velocidade = 80

if velocidade_atual > limite_velocidade:
    print(f"Voçê excedeu o limite em {velocidade_atual - limite_velocidade} km/h.\n"
          f"Valor da multa:R$ {(velocidade_atual - limite_velocidade)*7:.2f}".replace('.', ',')
    )
else:
    print(f'Na velocidade atual({velocidade_atual:.2f}KM/h) voçê nao receberá multa')