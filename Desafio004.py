"""Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
sobre ele."""
n = input('Insira qualquer caracter: ')
print('É numérico?', n.isnumeric())
print('É dígito?', n.isdigit())
print('É alfanumérico?', n.isalnum())
print('É do alfa?', n.isalpha())
print('É decimal?', n.isdecimal())
print('É indentifier?', n.isidentifier())
print('Está em caixa baixa?', n.islower())
print('Printable?', n.isprintable())
print('É espaço?', n.isspace())
print('Title?', n.istitle())
print('Está em caixa alta?', n.isupper())
