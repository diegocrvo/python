"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1.000,00.
C) Qual é o nome do produto mais barato.
----------------------------------------------------------------------------------------------"""
barato = ''
menor = total = count = maiormil = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    price = float(input('Digite o preço do produto: '))
    count += 1
    total += price
    if price > 1000:
        maiormil += 1
    if count == 1:
        menor = price
    if price < menor:
        barato = nome
    comando = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while comando not in 'SN':
        comando = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if comando == 'N':
        break
print(f'O total da compra é R${total}')
print(f'Um total de {maiormil} produtos custam mais que R$1.000,00')
print(f'O produto mais barato da lista é {barato}')
