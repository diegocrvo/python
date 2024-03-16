# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.
# -----------------------------------------------------------------------------

vel = float(input('Qual a velocidade do veículo?: '))
if vel > 80:
    print(f'Seu veículo foi multado! Você excedeu o limite permitido de 80km/h.'
          f'\nO valor da multa é de: R${(vel - 80) * 7.0:.2f}')
print('Velocidade permitida. Boa viagem!')
