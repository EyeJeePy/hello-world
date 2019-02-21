"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%."""
sal = float(input('Salário: R$ '))
if sal <= 1250:
    nusal = sal * 1.15
else:
    nusal = sal * 1.1

print('Quem recebia R${:.2f} passará a receber R${:.2f}.'.format(sal, nusal))
