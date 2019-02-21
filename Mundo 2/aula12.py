nome = str(input('Qual é o seu nome?\n')).strip().lower()
if nome == 'isadora':
    print('Que nome bonito!\n')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular, né?\n')
elif nome in 'celso wellington':
    print('Te amo tanto <3\n')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))