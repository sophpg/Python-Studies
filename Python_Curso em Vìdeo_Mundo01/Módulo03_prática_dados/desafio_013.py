# AUMENTO SALARIAL 

'''
-----------> COM AUMENTO DE 15% 

salário_atual = float(input('Insira o valor do salário atual: '))
novo_salário = salário_atual + (salário_atual * 0.15 / 100)

print('O novo salário é de: {:.2f} ' .format(novo_salário))

'''

# COM AUMENTO INSERIDO PELO USUÁRIO 

salário_atual = float(input('Informe o valor so salário atual: R$'))
inserir_desconto = int(input('Informe a porcentagem de aumento salarial: '))

porcentagem = inserir_desconto / 100
desconto = salário_atual * porcentagem
salário_final = salário_atual + desconto

print('O salário de R${:.2f}, com aumento de {}%, resulta em um novo salário de R${:.2f}.' .format(salário_atual, inserir_desconto, salário_final))
