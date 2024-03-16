"""Desenvolva um programa que leia o primeiro termo e a razão de
uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos
dessa progressão.
------------------------------------------------------------------------------------"""
pt = int(input('Digite um número: '))
r = int(input('Digite a razão: '))

dt = pt + (10 - 1) * r
for c in range(pt, dt + r, r):
    print(f'{c} ➔ ', end='')
print('ACABOU')
