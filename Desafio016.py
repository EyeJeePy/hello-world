"""Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira."""
import math
n = float(input('Digite um número real qualquer: '))
ni = math.trunc(n)
print('Sua porção inteira é {}.'.format(ni))
