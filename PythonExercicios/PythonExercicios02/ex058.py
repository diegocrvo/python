"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.
------------------------------------------------------------------------------------"""
from random import randint
from time import sleep  # Faz o computador dar uma pausa antes de apresentar o que vem posteriormente.
computador = randint(0, 10)  # Faz o computador "escolher" um número aleatório.

print('-=-' * 25)
print('Estou pensando em um número de 0 a 10... Tente adivinhar qual é esse número.')
print('-=-' * 25)

palpites = 0
acertou = False
while not acertou:
    jogador = int(input('Digite o número: '))
    palpites += 1
    print('Processando...')
    sleep(1)
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
        print('-' * 30)
if palpites == 1:
    print('\033[32mParabéns, você acertou e primeira!\033[m')
else:
    print(f'\033[32mVocê acetou!\033[33m Mas tentou {palpites} vezes até acertar.\033[m')
