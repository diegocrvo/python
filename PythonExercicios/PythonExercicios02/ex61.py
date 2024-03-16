"""Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
-----------------------------------------------------------------------------------"""
from time import sleep

print('\033[32m#\033[m' * 80)
print('\033[33m', end='')
print('GERADOR DE PA'.center(80))
print('\033[32m-\033[m' * 80)

prim_term = int(input('\033[36mDigite um número: \033[m'))
razao = int(input('\033[36mDigite a razão: \033[m'))
print('\033[32m-\033[m' * 80)

sleep(0.5)
c = 0
while c < 10:
    sleep(0.3)
    print(f'{prim_term}', end='')
    prim_term += razao
    sleep(0.3)
    print('\033[34m -> \033[m' if c % 2 == 0 else '\033[32m -> \033[m', end='')
    c += 1
sleep(0.3)
print('\033[33mACABOU!\033[m')
sleep(0.5)
print('\n\033[31mPrograma Encerrado.')