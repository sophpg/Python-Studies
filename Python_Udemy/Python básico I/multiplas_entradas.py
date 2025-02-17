# múltiplas entradas na mesma linha Input

dados = input('Digite o seu nome, idade e altura: ').split()

nome = dados[0]
idade = dados[1]
altura = dados[2]

print(f'O meu nome é {nome.upper()}, tenho {idade} anos de idade e tenho {altura} de altura') # o .upper() deixa somente aqule elemento como maiúsculos

''' é pedido um input, que é armazenado em dados
mas ao invés de armazenar tudo, pedimos para que faça um split com o que for digitado pelo usuário 
o split separa os espaços 
no index 0, é armazenada a informação da variável nome 
no index 1, é armazenada informação da variável idade '''