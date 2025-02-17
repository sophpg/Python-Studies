idade = int(input('Informe a sua idade: '))

if idade < 18:
    print('Criança')
elif 18 <= idade < 60:
    print('Maior de idade')
else:
    print('Idoso')