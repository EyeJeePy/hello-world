"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
progressão."""
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termos = int(input('Termos: '))
pa = primeiro + (termos - 1) * razão
for c in range(primeiro, pa + razão, razão):  ## pa + razão para que ele mostre o último termo, senão ficaria oculto
    print('{}'.format(c), end=' ¬ ')
print('Fim')