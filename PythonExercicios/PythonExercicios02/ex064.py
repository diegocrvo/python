"""Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando
o flag).
----------------------------------------------------------------------------------"""

# count = soma = entrada = 0
# while entrada != 999:
#     entrada = int(input('Digite um número [999 para parar]: '))
#     if entrada != 999:
#         soma += entrada
#         count += 1
# print(f'A soma dos {count} números digitados é {soma}.')

entrada = soma = count = 0
entrada = int(input('Digite um número: '))
while entrada != 999:
    soma += entrada
    count += 1
    entrada = int(input('Digite um número: '))
print(f'A soma dos {count} números digitados é {soma}.')
