"""Desenvolva um programa que pergunte a distância de uma viagem em quilômetros. Calcule o preço da passagem cobrando
R$0,50 por quilômetro para viagens de até 200km e R$0,45 para viagens mais longas."""
d = float(input('Insira a distância da viagem: '))

if d <= 200:
    p1 = d * 0.5
    print('Sua passagem custará R${}.'.format(p1))

else:
    p2 = d * 0.45
    print('Sua passagem custará R${}.'.format(p2))
