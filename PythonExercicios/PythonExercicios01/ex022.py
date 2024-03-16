# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas.
# - O nome com todas as letras minúsculas.
# - Quantas letras tem tudo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
# ---------------------------------------------------------------------
nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome maiúsculo é: {nome.upper()}')
print(f'Seu nome minúsculo é: {nome.lower()}')
print(f'Seu nome completo tem {len(nome.replace(' ', ''))} caracteres.')
# print(f'Seu primeiro nome é {nome.split()[0]} e tem {nome.find(' ')} caracteres.')
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} caracteres.')
