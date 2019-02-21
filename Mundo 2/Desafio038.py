"""Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
- O primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais"""
a = int(input('Número inteiro A: '))
b = int(input('Número inteiro B: '))

if a > b:
    print('O primeiro valor é maior.')

elif a == b:
    print('Não existe valor maior, os dois são iguais.')

else:
    print('O segundo valor é maior.')