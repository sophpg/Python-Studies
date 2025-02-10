# CALCULAR A MEDIDA DA HIPOTENUSA A PARTIR DOS CATETOS 

''' pelo cálculo matemático - sem importar 

cateto_oposto = float(input('Insira a medida do cateto oposto: '))
cateto_adjacente = float(input('Insira a medida do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)    #fórmula para calcular raiz ---> 1/número da raiz

print('A hipotenusa vai medir {:.2f}.' .format(hipotenusa))
'''

# importando math

import math 
cateto_oposto = float(input('Insira o valor do cateto oposto: '))
cateto_adjacente = float(input('Insira o valor do cateto adjacente: '))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)