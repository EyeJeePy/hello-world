"""Faça um programa que leia o sexo de uma pessoa, mas só aceita os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto."""
sexo = str(input('Qual é o seu sexo? [M/F] ')).strip().upper()[0]  # [0] o programa só lê a primeira letra
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Qual é o seu sexo? [M/F] ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso!')
if sexo == 'F':
    print('Sexo Feminino registrado com sucesso!')
