"""A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, conforme a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master
--------------------------------------------------------------------------------"""
from datetime import date

print('-' * 40)
print('Confederação Nacional de Natação'.center(40))
print('-' * 40)

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

print(f'Esse ano você faz {idade} ano(s).')

if idade <= 9:
    print('\033[31mCategoria MIRIM')

elif idade <= 14:
    print('\033[32mCategoria INFANTIL')

elif idade <= 19:
    print('\033[33mCategoria JUNIOR')

elif idade <= 25:
    print('\033[34mCategoria SÊNIOR')

else:
    print('\033[35mCategoria MASTER')
