"""Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
------------------------------------------------------------------------------------"""
from time import sleep

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite um valor: '))
print(f'{'-' * 35}')

comando = 0
while comando != 5:
    print("""O que gostaria de fazer:

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
""")
    comando = int(input('Digite um comando: '))
    if comando == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}.')
    elif comando == 2:
        produto = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} é {produto}.')
    elif comando == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior número digitado é {maior}.')
    elif comando == 4:
        print(f'{'-' * 35}')
        print('Digite os novos valores:')
        valor1 = float(input('Digite um valor: '))
        valor2 = float(input('Digite um valor: '))
    elif comando == 5:
        print('Finalizando...')
    else:
        print(f'Opção inválida. Tente novamente.'
              f'\n{'-' * 35}')

sleep(1)
print('')
print('\033[31mPrograma Encerrado!\033[m')
