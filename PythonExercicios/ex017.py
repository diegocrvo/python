# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e mostre
# o comprimento da hipotenusa.
# ----------------------------------------------------------------------
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = hypot(co, ca)
print(f'A hipotenusa mede: {h:.2f}!')
