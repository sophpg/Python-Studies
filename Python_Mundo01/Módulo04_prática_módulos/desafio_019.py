# SORTEIO DE NOMES 

import random # ou somente utilizar: from math import random

aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4] # em python, listas ficam entre colchetes[] e se coloca os itens que estão dentro da lista 
sorteio = random.choice(lista)

print('O aluno escolhido foi {}. ' .format(sorteio))