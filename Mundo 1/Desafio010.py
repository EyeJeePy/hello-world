"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$1,00 = R$3,27."""
r = float(input('Quantos reais você tem na carteira? R$'))
print('Com R${:.3f}, você conseguiria comprar US${:.3f}.'.format(r, r/3.27))
