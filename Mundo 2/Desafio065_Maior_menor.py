"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores."""
maior = 0
menor = 0
count = 0
opt = 'Ss'
med = 0
soma = 0
while opt in 'Ss':
    num = int(input('Insira um número: '))
    count += 1
    soma += num
    if count == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opt = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
med = soma / count
print('{}, {}, {}'.format(med, maior, menor))
