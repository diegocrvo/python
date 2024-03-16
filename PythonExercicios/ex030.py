# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR
# ou ÍMPAR.
# ----------------------------------------------------------------------------

num = int(input('Digite um número: '))
res = num % 2
if res == 0:
    print('Este número é PAR!')
else:
    print('Este número é ÍMPAR!')
