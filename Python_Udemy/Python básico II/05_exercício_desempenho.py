nota_aluno = float(input('Digite a nota do aluno: '))

if nota_aluno >=9:
    print('Parabéns! Você tirou um A!')
elif nota_aluno >=7:
    print('Bom trabalho! Você tirou um B!')
elif nota_aluno >=5:
    print('Você passou, mas precisa melhorar. Você tirou um C!')
else:
    print('Você não passou de ano :( ')