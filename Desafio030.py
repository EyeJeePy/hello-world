"""Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar."""
num = int(input('Insira um número inteiro: '))
div = (num % 2)

if div == 0:
    print('O número {} é par.'.format(num))

else:
    print('O número {} é ímpar.'.format(num))
