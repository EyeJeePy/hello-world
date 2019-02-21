"""Refaça o Desafio009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."""
num = int(input('Quero a tabuada do número: '))
lim = int(input('Quero multiplicar até o número: '))  # Não faz parte do exercício
for c in range(1, lim+1):  # lim+1 não faz parte do exercício, o original só vai até 11
    print('{} x {} = {}'.format(num, c, num*c))
