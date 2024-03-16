# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# -------------------------------------------------------------------------
from datetime import date
ano = int(input('Digite um ano para analise (coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
res4 = ano % 4
res100 = ano % 100
res400 = ano % 400
if res4 == 0 and res100 != 0 or res400 == 0:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é bissexto!')
