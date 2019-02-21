"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos:
Apos a sopa
A sacada da casa
A torra da derrota
O lobo ama o bolo
Anotaram a data da maratona
Race car"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Esta frase é um palíndromo!')
else:
    print('Não é um palíndromo.')
