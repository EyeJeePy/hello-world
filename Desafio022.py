"""Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas;
- O nome com todas minúsculas;
- Quantas letras no total, sem considerar espaços;
- Quantas letras tem o primeiro nome."""

nome = str(input('Nome completo: \n')).strip()
letras = len(nome) - nome.count(' ')
print(nome.upper())
print(nome.lower())
print(letras)
print(nome.find(' '))
