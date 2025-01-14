# PROGRAMA QUE LÊ UM NÚMERO INTEIRO E MOSTRA NA TELA O SEU SUCESSOR E SEU ANTECESSOR 

numero = int(input('Digite um número: '))
antecessor = numero - 1
sucessor = numero + 1

print('Ao analisar o valor {}, afirmamos que o seu antecessor é {} e o seu sucessor é {}.' .format(numero, antecessor, sucessor))

# OU PODE SER ESCRITO SEM GUARDAR VALOR DE ANTECESSOR E SUCESSOR EM VARIÁVEIS 
''' 
numero = int(input('Digite um número: '))
print('Ao analisar o valor {}, afirmamos que o seu antecessor é {} e o seu sucessor é {}.' .format(numero, (numero-1), (numero+1)))

'''