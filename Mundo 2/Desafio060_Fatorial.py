"""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120"""
fac = 1
num = int(input('Insira um número para obter seu fatorial: '))
while num > 0:
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    fac *= num
    num -= 1
print('{}'.format(fac))
