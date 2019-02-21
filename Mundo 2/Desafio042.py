"""Refaça o DESAFIO035 dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isóceles: dois lados iguais
- Escaleno: todos os lados diferentes"""
a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a < b + c and b < a + c and c < b + a:
    if a == b == c:
        print('Equilátero.')
    elif a == b or a == c or b == a or b == c:
        print('Isóceles.')
    else:
        print('Escaleno.')
else:
    print('Essa retas não formam um triângulo.')