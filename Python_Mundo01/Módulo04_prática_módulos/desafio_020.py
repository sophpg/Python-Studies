# SORTEIO DE ORDEM 

import random # ou somente utilizar: from math import random

nome1 = str(input('Primeira pessoa: '))
nome2 = str(input('Segunda pessoa: '))
nome3 = str(input('Terceira pessoa: '))
nome4 = str(input('Quarta pessoa: '))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)

print('A ordem das pessoas será: {}' .format(lista))