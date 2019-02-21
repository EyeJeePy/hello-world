"""Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
será negado."""
print('===EMPRÉSTIMO BANCÁRIO===')

casa = float(input('\nValor da casa: R$ '))
salario = float(input('\nSalário do comprador: R$ '))
anos = (float(input('\nAnos: ')))

mensal = (casa / (anos * 12))
limite = salario * 0.3

if mensal <= limite:
    print('Empréstimo aprovado! \nO pagamento será realizado em {} anos no valor de R${}.'.format(anos, mensal))

else:
    print('Empréstimo negado!')
