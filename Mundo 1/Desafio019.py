"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que o ajude
lendo o nome deles e escrevendo o nome do escolhido."""
from random import choices
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
alunos = [a1, a2, a3, a4]
print('{} irá apagar o quadro.'.format(choices(alunos)))
