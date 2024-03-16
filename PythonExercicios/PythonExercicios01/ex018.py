# Faça um programa que leia um ângulo qualquer e mostre na
# tela o valor do seno, cosseno e tangente desse ângulo.
# -------------------------------------------------------------
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo: '))
rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print(f'Estes são o seno: {seno:.2f}, '
      f'\ncosseno: {cosseno:.2f} '
      f'\ne a tangente: {tangente:.2f} de {ang}.')
