# Crie um programa que leia o nome de uma cidade e diga se ela começa ou
# não com o nome "SANTO".
# -----------------------------------------------------------------------
cidade = str(input('Digite o nome da cidade: ').strip())
print('Santo' == cidade.capitalize().split()[0])
