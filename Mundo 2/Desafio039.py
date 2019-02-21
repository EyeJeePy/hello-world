"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
import datetime
ano = datetime.date.today().year
jovem = int(input('Insira o ano de nascimento do jovem: '))

res = ano - 18

if jovem == res:
    print('É hora de se alistar!')

elif jovem < res:
    print('Já passou do tempo do alistamento.')

else:
    print('Ainda vai se alistar.')
