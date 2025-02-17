# Captura do valor do produto 
valor = float(input('Insira o valor do produto: '))

# Calcula o valor com 10% de acréscimo 
valor_acrescimo = valor + (valor * 10 / 100) # ou valor_acrescimo = valor * 1.10

# Exibir o valor final na tela 
print(f'O valor final do produto com acréscimo é: \n R${valor_acrescimo:.2f}') # o :.2f indica quantas casas decimais devem ser exibidas, no caso 2