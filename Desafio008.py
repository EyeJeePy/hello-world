"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""
mt = float(input('Insira um valor em metros: '))
c = mt * 10
mm = mt * 100
print('Ele equivale a {}cm ou {}mm.'.format(c, mm))
