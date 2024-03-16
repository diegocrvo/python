# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# -----------------------------------------------------------------------------

from random import randint
from time import sleep  # Faz o computador dar uma pausa antes de apresentar o que vem posteriormente.

print('-=-' * 25)
print('Estou pensando em um número de 0 a 5... Tente adivinhar qual é esse número.')
print('-=-' * 25)
num = int(input('Digite o número: '))
num_rand = randint(0, 5) # Faz o computador "escolher" um número aleatório.
print('Processando...')
sleep(3)
if num == num_rand:
    print("Parabéns, você acertou!")

else:
    print(f"Desculpe, o número que pensei foi {num_rand}")
