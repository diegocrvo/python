"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns
termos. O programa encerra quando ele disser que quer mostrar 0 termos.
-----------------------------------------------------------------------------------"""
from time import sleep

print('\033[32m#\033[m' * 80)
print('\033[33m', end='')
print('GERADOR DE PA'.center(80))
print('\033[32m-\033[m' * 80)

prim_term = int(input('\033[36mDigite um número: \033[m'))
razao = int(input('\033[36mDigite a razão: \033[m'))
print('\033[32m-\033[m' * 80)

sleep(1)
count = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while count <= total:
        sleep(0.3)
        print(f'{prim_term}', end='')
        prim_term += razao
        sleep(0.3)
        if count != total:
            print('\033[34m -> \033[m' if count % 2 == 0 else '\033[32m -> \033[m', end='')
        else:
            print('')
        count += 1
    print('\033[32m-\033[m' * 80)
    mais = int(input('\033[36mDeseja mostrar mais quantos termos?: \033[m'))
sleep(0.5)
print('\033[31mPrograma Encerrado.')
