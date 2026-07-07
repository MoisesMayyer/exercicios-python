import math
from math import radians

angulo= float(input('digite algum angulo'))
cos = math.cos(radians(angulo))
sen = math.sin(radians(angulo))
tan =(math.tan(radians(angulo)))
print('seu cos é {} sua tan é {} e seu sen é {:.2f}'.format(cos,tan,(sen)))
