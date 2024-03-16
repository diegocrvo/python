"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o Flag).
-------------------------------------------------------------------------------------------------------------------"""
count = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
    count += 1

print(f'A soma do(s) {count} valor(es) é {soma}')
