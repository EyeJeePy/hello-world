"""Crie um programa que faça o computador jogar Jokenpô com você."""
from random import randint
from time import sleep
usr = int(input('[ 1 ] PEDRA\n[ 2 ] PAPEL\n[ 3 ] TESOURA\nQual é a sua escolha?\n'))
comp = randint(1, 3)
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO\n')
sleep(0.3)
if usr == comp:
    print('Empate.')
elif usr == 1 and comp == 2:
    print('Computador: Papel\nPapel ganha de pedra. Você perdeu!')
elif usr == 1 and comp == 3:
    print('Computador: Tesoura\nPedra destrói tesoura. Você ganhou!')
elif usr == 2 and comp == 1:
    print('Computador: Pedra\nPapel ganha de pedra. Você ganhou!')
elif usr == 2 and comp == 3:
    print('Computador: Tesoura\nTesoura destrói papel. Você perdeu!')
elif usr == 3 and comp == 1:
    print('Computador: Pedra\nPedra destrói tesoura. Você perdeu!')
elif usr == 3 and comp == 2:
    print('Computador: Papel\nTesoura destrói papel. Você ganhou!')
