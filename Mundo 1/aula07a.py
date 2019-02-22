# ** Potência
# // Divisão inteira
# % Resto da divisão

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print('Prazer em te conhecer, {:20}!'.format(nome))
print('Prazer em te conhecer, {:>20}!'.format(nome))
print('Prazer em te conhecer, {:^20}!'.format(nome))
print('Prazer em te conhecer, {:<10}!'.format(nome))
print('Prazer em te conhecer, {:=^20}!'.format(nome)) # ordem dos caracteres em {}

# Soma de int #
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
# print('A soma vale {}.'.format(n1+n2))
s = n1 + n2
st = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, \no produto é {}, a divisão é {:.4f}.'.format(s, st, m, d), end=' ')
print('A divisão inteira é {} e potência {}.'.format(di, e))
