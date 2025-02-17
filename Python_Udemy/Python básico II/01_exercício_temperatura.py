temperatura = int(input('Informe a temperatura: '))

if temperatura <= 10:
    print('Muito frio.')
elif 10 < temperatura <= 20:
    print('Tempo fresco.')
else:
    print('Muito quente.')