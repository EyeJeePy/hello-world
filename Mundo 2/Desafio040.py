"""Crie um programa que leia duas notas de um aluno e calcule sua média mostrando uma mensagem no final de acordo com
a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO"""
a = float(input('Nota A: '))
b = float(input('Nota B: '))
med = (a + b) / 2
if med < 5:
    print('# REPROVADO #')
elif med >= 7:
    print('.~*¨ \033[1mAPROVADO!\033[m ¨*~.')
else:
    print('!!! RECUPERAÇÃO !!!')
