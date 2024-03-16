"""Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores 'M' ou 'F'.
Caso esteja errado peça a digitação novamente até ter um valor correto.
----------------------------------------------------------------------------------------"""

sexo = str(input('Qual seu sexo? [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('\033[31mDados inválidos. Qual seu sexo? [M/F]: \033[m')).strip().upper()[0]

if sexo in 'mM':
    sexo = 'Masculino'
if sexo in 'fF':
    sexo = 'Feminino'
print(f'O sexo registrado é {sexo}.')
