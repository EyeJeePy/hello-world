"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada quilômetro acima do limite."""
vel = float(input('Velocidade do veículo: '))
acres = ((vel - 80) * 7)
if vel <= 80:
    print('Velocidade {}'.format(vel))

else:
    print(f'Velocidade máxima ultrapassada! \nVocê foi multado em R${acres}.')
