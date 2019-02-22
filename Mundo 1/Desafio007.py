# Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média. #
p = float(input('Português: '))
m = float(input('Matemática: '))
h = float(input('História: '))
g = float(input('Geografia: '))
c = float(input('Ciências: '))
ma = (p+m+h+g+c)/5
mi = (p+m+h+g+c)//5
print('A média é {}, a média inteira é {}'.format(ma, mi))
