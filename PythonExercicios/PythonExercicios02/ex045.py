"""Crie um programa que faça o computador jogar Jokenpô com você.
--------------------------------------------------------------------------------"""
'''from time import sleep
from random import randint

print('*' * 30)
print('JOKENPÔ'.center(30))
print('*' * 30)
print('Iniciando...')

sleep(1)

print('Hello!\n'.center(30))

sleep(1)

print('Escolha pedra, papel ou tesoura:\n')
print('1 = Pedra'
      '\n2 = Papel'
      '\n3 = Tesoura')
jogador = int(input('Digite 1, 2 ou 3: '))
print('')

maq = randint(1, 3)
if maq == 1:
    maq = 'Pedra'
elif maq == 2:
    maq = 'Papel'
elif maq == 3:
    maq = 'Tesoura'

sleep(1)

if jogador == 1:
    jogador = 'Pedra'
elif jogador == 2:
    jogador = 'Papel'
elif jogador == 3:
    jogador = 'Tesoura'
else:
    print('\033[31mEntrada Inválida.')

if jogador in ['Pedra', 'Papel', 'Tesoura']:
    print(f'Você escolheu: {jogador}'.center(30))
    print('X'.center(30))
    sleep(1)
    print(f'Eu escolhi: {maq}'.center(30))

if maq == jogador:
    sleep(1)
    print('\033[33mEMPATAMOS!'.center(35))

elif (maq == 'Pedra' and jogador == 'Tesoura') or (maq == 'Tesoura' and jogador == 'Papel') or (maq == 'Papel' and jogador == 'Pedra'):
    sleep(1)
    print('\033[31mVOCÊ PERDEU!'.center(35))

elif (maq == 'Tesoura' and jogador == 'Pedra') or (maq == 'Pedra' and jogador == 'Papel') or (maq == 'Papel' and jogador == 'Tesoura'):
    sleep(1)
    print('\033[32mVOCÊ VENCEU!'.center(35))
----------------------------------------------------------------------------------------'''
from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('')
print('*' * 30)
print('JOKENPÔ'.center(30))
print('*' * 30)
print('Iniciando...'.center(30))

sleep(1)

print('Hello!\n'.center(30))

sleep(1)

jogador = int(input('''Escolha pedra, papel ou tesoura:

[ 0 ] = Pedra
[ 1 ] = Papel
[ 2 ] = Tesoura

Digite 0, 1 ou 2: '''))
print('')

sleep(1)
print('\033[32mJO'.center(10))
sleep(1)
print('\033[35mKEN'.center(20))
sleep(1)
print('\033[36mPÔ!!!\033[m'.center(40))
print('')

print('-=' * 15)
print(f'Você escolheu: {itens[jogador]}'.center(30))
print('X'.center(30))
print(f'Eu escolhi: {itens[computador]}'.center(30))
print('-=' * 15)

sleep(1)

if computador == 0:  # Computador jogar PEDRA
    if jogador == 0:
        print('\033[33mEMPATAMOS!'.center(35))

    elif jogador == 1:
        print('\033[32mVOCÊ VENCEU!'.center(35))

    elif jogador == 2:
        print('\033[31mVOCÊ PERDEU!'.center(35))

    else:
        print('\033[34mJOGADA INVÁLIDA!'.center(35))


elif computador == 1:  # Computador jogar PAPEL
    if jogador == 0:
        print('\033[31mVOCÊ PERDEU!'.center(35))

    elif jogador == 1:
        print('\033[33mEMPATAMOS!'.center(35))

    elif jogador == 2:
        print('\033[32mVOCÊ VENCEU!'.center(35))

    else:
        print('\033[34mENTRADA INVÁLIDA!'.center(35))


elif computador == 2:  # Computador jogar TESOURA
    if jogador == 0:
        print('\033[32mVOCÊ VENCEU!'.center(35))

    elif jogador == 1:
        print('\033[31mVOCÊ PERDEU!'.center(35))

    elif jogador == 2:
        print('\033[33mEMPATAMOS!'.center(35))

    else:
        print('\033[34mENTRADA INVÁLIDA!'.center(35))
