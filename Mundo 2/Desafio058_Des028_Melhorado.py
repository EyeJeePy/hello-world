"""Melhore o jogo do Desafio028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
num = randint(0, 10)
count = 1
print('#'*9 JOGO DA ADIVINHAÇÃO '#'*9\n')
print('Tente adivinhar um número entre 0 e 10')
print('\033[7m+{}+\033[0m'.format(num))
usrnum = int(input('Qual é o número? '))
while usrnum != num:
    if usrnum > 10 or usrnum < 0:
        print('\n\033[1mDeve ser um número entre \033[1;4m0 e 5\033[0m\033[1m!\033[0m')
    usrnum = int(input('\033[1;31mErrou!\033[0m Tente novamente:\033[0m '))
    count += 1
print('\033[1;36;40mParabéns! Você adivinhou!\033[0m\n'
      '\033[1;36;40mForam necessárias {} tentativas.\033[0m'.format(count))
