"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
from math import sin, cos, tan
a = float(input('Insira um ângulo: '))
print("Sen = {}".format(sin(a)))
print("Cos = {}".format(cos(a)))
print("Tan = {}".format(tan(a)))
