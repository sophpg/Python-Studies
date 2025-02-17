horário = float(input('Informe o horário no momento: '))   

if horário < 12:
    print('Bom dia!')
elif 12 <= horário < 18:
    print('Boa tarde!')
else:
    print('Boa noite!')