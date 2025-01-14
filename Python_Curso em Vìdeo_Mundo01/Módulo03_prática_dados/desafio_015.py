# EXERCÍCIO PARA CÁLCULO DE VALOR DE ALUGUEL DE CARRO DE ACORDO COM DIAS E KMS RODADOS 

dias = int(input('Qual a quantidade de dias que o carro foi utilizado? '))
km = float(input('Quantos kilômetros foram rodados? '))

total = (dias * 60) + (km * 0.15)

print('O total do custo de acordo com os {} dias utilizados e {} km rodados é de R${:.2f}.' .format(dias, km, total))