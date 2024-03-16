"""Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
-------------------------------------------------------------------------------"""
frase = str(input('Digite uma frase: ')).strip().upper()
junto = frase.replace(' ', '')
inverso = junto[::-1]

'''inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

if inverso == junto:
    print(f'\033[32mA frase "{frase}" invertido fica "{inverso}" e É um PALÍNDROMO.')
else:
    print(f'\033[31mA frase "{frase}" invertido fica "{inverso}" e NÃO é um PALÍNDROMO.')
