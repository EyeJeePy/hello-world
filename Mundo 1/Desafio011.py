"""Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²."""
lar = float(input('Largura da parede em metros: '))
hei = float(input('Altura da parede em metros: '))
print('A parede tem {}m².'.format(lar*hei), end=' ')
print('Serão necessários {}L de tinta para pintá-la.'.format((lar*hei)/2))
