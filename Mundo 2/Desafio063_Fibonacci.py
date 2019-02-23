"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência
de Fibonacci.
Exemplo: 0 → 1 → 1 → 2 → 3 → 5 → 8"""
# F(x) = F(x-1) + F(x-2)
c = 0
t1 = 0
t2 = 1
n = int(input('Número de elementos: '))
print('{} >>> {}'.format(t1, t2), end='')

while c <= n:
    t3 = t1 + t2
    print(' >>> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('\nFIM')
