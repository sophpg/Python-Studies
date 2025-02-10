# PROGRAMA QUE LÊ O ÂNGULO E DÁ O SEU SENO, COSSENO E TANGENTE

import math # ou utilizando somente: from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print('O SENO de {} é igual a {:.2f}.' .format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O COSSENO {} é igual a {:.2f}.' .format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('A TANGENTE de {} é igual a {:.2f}.' .format(angulo, tangente))
