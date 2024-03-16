# Crie um programa que leia um número real qualquer pelo teclado e mostre na
# tela a sua porção inteira.
# Ex. Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.
# -------------------------------------------------------------------
'''from math import trunc
num = float(input('Digite um número: '))
print(f'A porção inteira do número {num} é {trunc(num)}.')'''

num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')
