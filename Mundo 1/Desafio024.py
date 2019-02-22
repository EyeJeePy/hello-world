"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'."""
cidade = str(input('Cidade: ')).strip().lower()
print('santo' in cidade)
