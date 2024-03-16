"""Faça um programa que leia um número inteiro e diga se ele é ou não
um número primo.
-----------------------------------------------------------------------------------"""
n = int(input('Digite um número: '))
total = 0
for p in range(1, n + 1):
    if n % p == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{p} ', end='')
print(f'\n\033[mO número {n} foi dividido {total} vezes.')
if total == 2:
    print(f'Ele foi dividido apenas por 1 e por ele mesmo.'
          f'\nPortanto o número {n} É PRIMO.')
else:
    print(f'Portanto o número {n} NÃO É PRIMO.')
