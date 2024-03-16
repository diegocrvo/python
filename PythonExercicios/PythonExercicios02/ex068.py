"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele
conquistou no final do jogo.
--------------------------------------------------------------------------------------------"""
from random import randint

count = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um número: '))
    escolha_jogador = str(input('Escolha PAR ou ÍMPAR [P/Í]: ')).strip().upper()[0]
    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Escolha PAR ou ÍMPAR [P/Í]: ')).strip().upper()[0]
    print('-' * 30)
    soma = pc + jogador
    if soma % 2 == 0:
        if escolha_jogador == 'P':
            print('\033[32mVocê venceu!\033[m')
            print(f'Você jogou {jogador} e o computador jogou {pc}.')
            print(f'Total = {soma}')
            print('Vamos jogar novamente...')
            print('-' * 30)
            count += 1
        else:
            break
    else:
        if escolha_jogador == 'I':
            print('\033[32mVocê venceu!\033[m')
            print(f'Você jogou {jogador} e o computador jogou {pc}.')
            print(f'Total = {soma}')
            print('Vamos jogar novamente...')
            print('-' * 30)
            count += 1
        else:
            break

print('\033[31mVocê perdeu!\033[m')
print(f'Você jogou {jogador} e o computador jogou {pc}.')
print(f'Total = {soma}')
print(f'\033[33mNessa partida você ganhou {count} veze(s).')
