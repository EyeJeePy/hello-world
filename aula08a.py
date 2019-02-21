# import math  # para importar toda a biblioteca

from math import sqrt, floor  # ctrl+espaço para mostrar a lista de funcionalidades /
num = int(input('Digite um número: '))

# raiz = math.sqrt(num)
# print('A raiz de {} é {}.'.format(num, raiz))
# print('A raiz de {} é {}.'.format(num, math.ceil(raiz)))
# print('A raiz de {} é {}.'.format(num, math.floor(raiz)))
# print('A raiz de {} é{:0.3f}.'.format(num, raiz))

raiz = sqrt(num)  # com 'from math import sqrt' não é necessário informar a biblioteca na função
print('A raiz de {} é {}.'.format(num, floor(raiz)))
