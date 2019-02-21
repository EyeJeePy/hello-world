print('\033[4;1;41;30mOlar, mundo!\033[m\n')

print('\033[7;1;30mHoje é dia 15 de dezembro de 2018.\033[m\n\n')

coresl = {'branco': '\033[30m',
          'vermelho': '\033[31m',
          'verde': '\033[32m',
          'amarelo': '\033[33m',
          'azul': '\033[34m',
          'magenta': '\033[35m',
          'ciano': '\033[36m',
          'cinza': '\033[37m'}  # cor da letra

coresf = {'branco': '\033[1;40m',
          'vermelho': '\033[1;41m',
          'verde': '\033[1;42m',
          'amarelo': '\033[1;43m',
          'azul': '\033[1;44m',
          'magenta': '\033[1;45m',
          'ciano': '\033[1;46m',
          'cinza': '\033[1;47m'}  # cor do fundo

style = {'none': '\033[0m',
         'bold': '\033[1m',
         'underline': '\033[4m',
         'negative': '\033[7m'}  # estilo da fonte

print('\033[1;4mCores das letras:\033[m')
print('{}Branco'.format(coresl['branco']))
print('{}Vermelho'.format(coresl['vermelho']))
print('{}Verde'.format(coresl['verde']))
print('{}Amarelo'.format(coresl['amarelo']))
print('{}Azul'.format(coresl['azul']))
print('{}Magenta'.format(coresl['magenta']))
print('{}Ciano'.format(coresl['ciano']))
print('{}Cinza{}\n'.format(coresl['cinza'], '\033[m'))

print('\033[1;4mCores do fundo:\033[m')
print('{}Branco{}'.format(coresf['branco'], '\033[m'))
print('{}Vermelho{}'.format(coresf['vermelho'], '\033[m'))
print('{}Verde{}'.format(coresf['verde'], '\033[m'))
print('{}Amarelo{}'.format(coresf['amarelo'], '\033[m'))
print('{}Azul{}'.format(coresf['azul'], '\033[m'))
print('{}Magenta{}'.format(coresf['magenta'], '\033[m'))
print('{}Ciano{}'.format(coresf['ciano'], '\033[m'))
print('{}Cinza{}\n\n'.format(coresf['cinza'], '\033[m'))

print('\033[1;4mEstilos de fonte:\033[m')
print('{}None'.format(style['none']))
print('{}Bold{}'.format(style['bold'], '\033[m'))
print('{}Underline{}'.format(style['underline'], '\033[m'))
print('{}Negative\033[m'.format(style['negative']))
