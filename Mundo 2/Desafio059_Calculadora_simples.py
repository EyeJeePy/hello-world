"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
from time import sleep
print('\n>>> Insira dois números inteiros para acessar as opções de comando.')
num1 = int(input('\n1º valor: '))
num2 = int(input('2º valor: '))
sleep(.5)
usrchoice = 0
while usrchoice != 5:
    usrchoice = int(input('\n[ 1 ] Somar\n'
                          '[ 2 ] Multiplicar\n'
                          '[ 3 ] Maior\n'
                          '[ 4 ] Novos números\n'
                          '[ 5 ] Sair do programa\n'
                          'Escolha uma opção: '))
    sleep(.3)
    if usrchoice == 1:
        print('\n{} + {} = {}.'.format(num1, num2, num1 + num2))
    sleep(.3)
    if usrchoice == 2:
        print('\n{} x {} = {}'.format(num1, num2, num1 * num2))
    sleep(.3)
    if usrchoice == 3:
        if num1 > num2:
            print('\n{} > {}, ou seja, o maior deles é o {}.'.format(num1, num2, num1))
        else:
            print('\n{} > {}, ou seja, o maior deles é o {}.'.format(num2, num1, num2))
    sleep(.3)
    if usrchoice == 4:
        num1 = int(input('\n1º valor: '))
        num2 = int(input('2º valor: '))
    sleep(.3)
    if usrchoice > 5 or usrchoice < 1:
        print('\n\033[1mInsira uma opção válida!\033[0m')
print('\n=== FIM ===')