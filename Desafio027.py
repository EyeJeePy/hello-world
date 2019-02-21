"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente."""
nome = str(input('Nome: ')).strip().split()
primeiro = nome[0]
print(primeiro)
ultimo = nome[-1]
print(ultimo)
