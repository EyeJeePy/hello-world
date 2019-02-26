"""Melhore o Desafio061 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos."""
print('\033[7m === CALCULADORA DE PROGRESSÃO ARITMÉTICA === \033[0m')
num = int(input('Insira o primeiro termo: '))
raz = int(input('Insira a razão: '))
ter = int(input('Insira quantos termos: '))
count = 1
mais = 1
while mais != 0:
    while count <= ter:
        count += 1
        res = num + (count - 1) * raz
        print('{}'.format(res), ' → ' if count <= ter else '', end='')
    mais = int(input('\nCalcular mais termos: '))
    ter += mais
print('\nForam calculados {} termos da PA.'.format(ter))
print('\n\033[7m', '=' * 19, ' FIM ', '=' *19, '\33[0m')
