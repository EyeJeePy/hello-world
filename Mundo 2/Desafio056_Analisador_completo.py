"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""
somaidade = 0
mediaidade = 0
maior_idade_homem = 0
nome_velho = 0
tot_mulher_20 = 0
for p in range(1, 5):
    print('=== {}ª pessoa ==='.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [H/M]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Hh':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Hh' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade < 20:
        tot_mulher_20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem, nome_velho))
print('Ao todo são {} mulheres abaixo de 20 anos.'.format(tot_mulher_20))
