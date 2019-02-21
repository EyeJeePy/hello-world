"""Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez."""
frase = str(input('Frase: ')).strip().lower()
print('\nTotal de {} "A".'.format(frase.count('a')))
print('O "A" aparece pela primeira vez na posição {}.'.format(frase.find('a')))
a = frase.rfind('a')
print('O último "A" aparece na posição {}.'.format(a))
