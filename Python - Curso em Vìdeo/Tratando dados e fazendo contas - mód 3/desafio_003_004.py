
# DESAFIO 003 - EXIBIR SOMA ENTRE DOIS NÚMEROS INTEIROS
n1 = (int(input('Insira um número inteiro: ')))
n2 = (int(input('Insira outro número inteiro: ')))
soma = n1 + n2

print('A soma entre {} e {} é igual a {}' .format(n1, n2, soma))

# DESAFIO 004 - EXIBIR TODOS OS TIPOS DE INFORMAÇÕES POSSÍVEIS UTILIZANDO info.is
info = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', type(info))
print('Só tem espaços? ', info.isspace())
print('É um número? ', info.isnumeric())
print('É alfabético? ', info.isalpha())
print('É alfanumérico? ', info.isalnum())
print('Está em maiúsculas? ', info.isupper())
print('Está em minúsculas? ', info.islower())
print('Está capitalizado? ', info.istitle())
