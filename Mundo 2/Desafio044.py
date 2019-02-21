"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
1 - À vista dinheiro/cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros"""

cond = int(input("""Forma de pagamento:\n1 - À vista dinheiro/cheque\n2 - À vista no cartão\n3 - Em até 2x no cartão
4 - 3x ou mais no cartão\n>>> """))
preco = float(input('\nValor do produto: R$ '))

if cond == 1:
    print('Valor final: R$ {:.2f} com desconto de 10%.'.format(preco * 0.9))
elif cond == 2:
    print('Valor final: R$ {:.2f} com desconto de 5%.'.format(preco * 0.95))
elif cond == 4:
    print('Valor final: R$ {:.2f} com juros de 20%.'.format(preco * 1.2))
else:
    print('O valor final se mantém em R$ {:.2f}'.format(preco))