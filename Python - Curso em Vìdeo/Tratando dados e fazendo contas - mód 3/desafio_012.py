# DESCONTO DE PRODUTOS 

'''
----------> COM DESCONTO DE 5%

preço_original = float(input('Insira o preço do produto: '))
preço_final = preço_original - (preço_original * 5 / 100) 

print('O preço final é: {}' .format(preço_final))

'''

# -----------> COM DESCONTO INSERIDO PELO USUÁRIO 
preço_orig = float(input('Insira o preço do produto: R$'))
valor_desconto = int(input('Insira a porcentagem de desconto: '))

porcentagem = valor_desconto / 100
desconto = preço_orig * porcentagem
valor_final = preço_orig - desconto

print('O preço inicial de R${:.2f} com desconto de {}% gera um preço final de R${:.2f}.' .format(preço_orig, valor_desconto, valor_final))
