"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag)."""
c = 0
n = 0
s = 0
n = float(input('Somador de Entradas\n'
                'Insira o número [999 para sair]: '))
while n != 999:
    s += n
    c += 1
    print('>>> {}'.format(s))
    n = float(input('Insira o número [999 para sair]: '))
print('Você digitou {} números cuja soma é {}.'.format(c, s))
