"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
-------------------------------------------------------------------------------------"""
from time import sleep

comando = 'S'
count = soma = média = menor = maior = 0
while comando in 'Ss':
    print('-' * 45)
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    comando = str(input('Deseja continuar? [S/N]: ').upper()).strip()[0]
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

sleep(1)
media = soma / count
print('-' * 45)
print(f'\033[32mA média de todos os números digitados é {media:.2f}.\033[m')
sleep(0.5)
print(f'\033[33mO maior valor digitado foi {maior}.\033[m')
sleep(0.5)
print(f'\033[34mO menor valor digitado foi {menor}.\033[m')
