# Manipulação de string #
frase = 'Curso em Vídeo Python'

# Fatiamento #
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])  # melhor do que endereçar o último caracter desejado
print(frase[::2])
print(frase[9::3], '\n')

# Análise #
print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase, '\n')

# Transformação #
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title(), '\n')

frase2 = '   Aprenda Python  '  # espaços desnecessários
print(frase2)
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip(), '\n')

# Divisão #
print(frase.split(), '\n')

# Junção #
print('-'.join(frase), '\n')

# Diversos #
print("""Lorem ipsum venenatis donec arcu vestibulum sodales aptent nullam id nullam, dictum neque mollis nunc proin
tortor condimentum integer dictum donec, fusce enim vehicula habitant pretium eu aliquam elit sapien. posuere etiam
taciti laoreet blandit ornare adipiscing non sem, nibh cras potenti habitasse risus etiam tempor, magna proin velit
turpis litora quisque imperdiet. hac placerat etiam justo proin vitae diam, per consectetur egestas lacinia iaculis
sollicitudin consectetur, arcu blandit sed non pretium. adipiscing dictum torquent lorem curae dictumst euismod
molestie risus bibendum, libero magna tempor iaculis molestie viverra enim tristique ut congue, dolor tellus sed leo
duis sociosqu quisque accumsan. """, '\n')  # para dividir o texto

# Observação #
objeto = 'Mutação de objetos. Palavra de troca: maçã.'
print(objeto)
objeto = objeto.replace('maçã', 'banana')
print(objeto)
