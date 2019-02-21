"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal"""
usr = int(input('Insira um número inteiro: '))
opção = int(input('Escolha uma das opções:\n[ 1 ] BINÁRIO\n[ 2 ] OCTAL\n[ 3 ] HEXADECIMAL\n> '))
if opção == 1:
    print('{} convertido para BINÁRIO é {}.'.format(usr, bin(usr)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é {}.'.format(usr, oct(usr)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(usr, hex(usr)[2:]))
else:
    print('Opção inválida. Tente novamente!')