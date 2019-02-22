"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor."""
a = int(input('Escolha três números. \nA: '))
b = int(input('B: '))
c = int(input('C: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior é o {} e o menor é o {}.'.format(maior, menor))
