"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER"""
from datetime import date
atleta = int(input('Data de nascimento do atleta: '))
res = (date.today().year) - atleta

if res <= 9:
    print('Categoria MIRIM')
elif res <= 14:
    print('Categoria INFANTIL')
elif res <= 19:
    print('Categoria JUNIOR')
elif res <= 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER')