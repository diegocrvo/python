"""Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
---------------------------------------------------------------------------------"""
from datetime import date

anor = date.today().year - 18
atingiu = 0
nao = 0
for c in range(0, 7):
    data = int(input('Digite o ano de nascimento: '))
    if data <= anor:
        atingiu += 1
    else:
        nao += 1

print(f'{atingiu} pessoas já atingiram a maior idade e '
      f'\n{nao} ainda não atingiram a maior idade.')
