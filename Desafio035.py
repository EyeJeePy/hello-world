"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
triângulo."""
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a < b + c and b < a + c and c < b + a:
    print('Essas retas podem formar um triângulo!')

else:
    print('Essa retas não formam um triângulo.')
