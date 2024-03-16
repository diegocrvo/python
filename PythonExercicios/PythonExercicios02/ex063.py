"""Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma Sequência de Fibonacci.
Ex.: 0 -> 1 → 1 → 2 → 3 → 5 → 8
--------------------------------------------------------------------------------"""
from time import sleep

print('\033[36m-\033[33m' * 40)
print('SEQUÊNCIA DE FIBONACCI'.center(40))
print('\033[36m-' * 40)

num = int(input('\033[33mDigite um número: \033[m'))
t1 = 0
t2 = 1
print('\033[36m-' * 40)
print(f'\n\033[33m{t1}\033[m -> ', end='')
sleep(0.3)
print(f'\033[31m{t2}\033[m -> ', end='')
count = 3
while count <= num:
    sleep(0.3)
    t3 = t1 + t2
    print(f'\033[31m{t3}\033[m -> ' if count % 2 == 0 else f'\033[33m{t3}\033[m -> ', end='')
    t1 = t2
    t2 = t3
    count += 1
print('\033[32mFim.\033[m\n')
print('\033[36m-' * 40)
