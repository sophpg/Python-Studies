n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))

soma = n1 + n2
subtração = n1 - n2
divisão = n1 / n2
multiplicação = n1 * n2
divisão_inteira = n1 // n2
resto = n1 % n2
exponenciação = n1 ** n2

print('A soma é igual a {}, a subtração é igual a {}, a divisão é igual a {:.2f}, a multiplicação é igual a {}' .format(soma, subtração, divisão, multiplicação), end='')
print('A divisão inteira é igual a {}, o resto da divisão é igual a {} e a exponenciação é igual a {}.' .format(divisão_inteira, resto, exponenciação))

# para limitar o número de casas decimais utilizar {:.xf}, sendo x o número de casas que deseja que sejam exibidas
# para não ocorrer quebra de linha entre um print e outro, utilizar end='' no final do print
# para inserir quebra de texto em um print, utilizar \n

print('Teste de exclusão de quebra de linha', end=' >>> ')
print('continuação do teste')