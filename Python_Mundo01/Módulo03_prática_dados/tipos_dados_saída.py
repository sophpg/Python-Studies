# int - números inteiros - 7, -4, 0, 87145
# float - números decimais - 4.5, 0.005, -15.47
# bool - true or false 
# str - Texto - sempre colocado entre aspas simples ou duplas 


#diferentes formas de sintaxe 
soma = 10

print('A soma é igual a:', soma)

print('A soma é igual a: {}' .format(soma))

print(f'A soma é igual a: {soma}')


# utilizando o .format()
n1 = (int(input('Digite um valor: ')))
n2 = (int(input('Digite outro valor: ')))
soma = n1 + n2

print('O resultado da soma é igual a {} mais {} que resulta {}.' .format(n1, n2, soma))

# descobrundo o tipo de dado 
n1 = int(input('Digite um valor: '))  
print(type(n1))

# quando utilizado o int no início - se transforma em número - possível fazer somas 
# quando utilizado o str - permanece como string - texto
# quando utilizado o float, o número aparece com casa decimal 
# quando utilizado o bool, aparece false quando não existe um número inserido e true caso tenha um número inserido 


# MÉTODOS DE TESTE DE TIPO 
n = input('Insira algo: ')
print(n.isnumeric) # existem diversas opções no .is...
#é possível testar os dados 