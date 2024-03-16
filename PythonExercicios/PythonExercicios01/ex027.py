# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.
# Ex.: Ana Maria de Souza
# primeiro= Ana
# último= Souza
# ------------------------------------------------------------------------------
nome = str(input('Digite seu nome: ')).strip()
print(f'Primeiro nome: {nome.split()[0]}'
      f'\nÚltimo nome: {nome.split()[-1]}')
#      f'\nÚltima nome: {nome.split()[len(nome.split()) - 1]}')
