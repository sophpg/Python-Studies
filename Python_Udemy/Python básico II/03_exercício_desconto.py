valor_compra = float(input('Digite o valor da compra: R$'))

if valor_compra > 200:
    desconto = 0.2
elif valor_compra > 100: 
    desconto = 0.1
else:
    desconto = 0.05

valor_final = valor_compra - (valor_compra * desconto)
print(f'O valor final com desconto é de: R${valor_final:.2f}')
