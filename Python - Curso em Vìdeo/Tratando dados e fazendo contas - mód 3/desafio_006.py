numero = int(input('Insira um número: '))

dobro = 2 * numero
triplo = 3 * numero
raiz_quadrada = numero ** (1/2) # OU UTILIZAR ----> pow(numero, (1/2))

print('O dobro de {} é igual a {}.' .format(numero, dobro))
print('O triplo de {} é igual a {}.' .format(numero, triplo))
print('A raíz quadrada de {} é igual a {:.2f}' .format(numero, raiz_quadrada))

# OU - FAZER OPERAÇÕES SEM ARMAZENÁ-LAS EM VARIÁVEIS 

''' 
numero = int(input('Insira um número: '))

print('O dobro de {} é igual a {}.' .format(numero, (numero*2)))
print('O triplo de {} é igual a {}.' .format(numero, (numero*3)))
print('A raíz quadrada de {} é igual a {:.2f}' .format(numero, (numero**(1/2))))

'''
