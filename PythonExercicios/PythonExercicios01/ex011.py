# Faça um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo
# que cada litro de tinta pinta uma área de 2M².
la = float(input('Digite a largura: '))
al = float(input('Digite a altura: '))
a = la * al
print(f'Área total em m2²: \033[32m{a}m²\033[m'
      f'\nSerá necessário \033[33m{round(a / 2)}\033[m litros de tinta para pintá-la.')
