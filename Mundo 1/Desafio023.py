"""Faça um programa que leia um número de 9 a 9999 e mostre na tela cada um dos dígitos separados.
1834 = unidade:4; dezena:3; centena:8; milhar:1"""
num = str(input('Insira um número entre 9 e 9999: '))
u = num[3]
d = num[2]
c = num[1]
m = num[0]
print('Unidade: {}\n Dezena: {}\n Centena: {}\n Milhar: {}'.format(u, d, c, m))
