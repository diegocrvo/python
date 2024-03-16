# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.
# --------------------------------------------------------------------------
from random import shuffle
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem ficou:'
      f'\n{lista}')
