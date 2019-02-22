"""Refaça o Desafio051 lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""
print('\033[7m === CALCULADORA DE PROGRESSÃO ARITMÉTICA === \033[0m')
c = 0
num = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão: '))
ter = int(input('Insira quantos termos: '))
print('{}'.format(num), end=' → ')
while c < ter:
    c += 1
    num += raz
    print('{}'.format(num), ' → ' if c < ter else '', end='')
print('\n\n\033[7m =================== FIM =================== \033[0m')
