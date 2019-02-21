n1 = float(input('N1: '))
n2 = float(input('N2: '))
m = (n1 + n2)/2
print('Sua média é: {:.1f}.'.format(m))

if m >= 6:
    print('Parabéns! Sua média é boa!')

else:
    print('Sua média é ruim.')