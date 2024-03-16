# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o salário atual: R$'))
print(f'Novo salário, com 15% de aumento: R${s + (s * 15) / 100}')
