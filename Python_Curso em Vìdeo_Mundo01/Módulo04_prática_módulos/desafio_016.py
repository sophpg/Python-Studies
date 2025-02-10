# PROGRAMA QUE LÊ NUMERO REAL QUALQUER E MOSTRA SUA PORÇÃO INTEIRA 

''' 
UTILIZANDO TRUNC

from math import trunc

numero = float(input('Digite um número real para descobrir seu valor inteiro: '))
print('O valor digitado foi {} e o inteiro desse valor é {}.' .format(numero, trunc(numero)))
'''

# UTILIZANDO RECURSO INTERNO "INT"

numero = float(input('Digite um número real para descobrir seu valor inteiro: '))
print('O valor digitado foi {} e o seu inteiro é igual a {}.' .format(numero, int(numero)))