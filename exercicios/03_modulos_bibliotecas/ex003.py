# exercício 003 - seno, cosseno e tangente de um angulo
import math
from math import radians

angulo = float(input('digite o valor do angulo: '))
cos = math.cos(radians(angulo))
sen = math.sin(radians(angulo))
tan = math.tan(radians(angulo))

print(
    f"Ângulo:   {angulo}°\n"
    f"Cosseno:  {cos:.2f}\n"
    f"Seno:     {sen:.2f}\n"
    f"Tangente: {tan:.2f}"
)