"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 até 0 com uma pausa de 1 segundo entre eles.
---------------------------------------------------------------------------------------"""
import emoji
from time import sleep

for s in range(10, -1, -1):
    print(f'\033[33m{s} ')
    sleep(1)
print(emoji.emojize(':fireworks:'))
