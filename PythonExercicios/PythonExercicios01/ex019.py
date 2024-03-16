# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo
# o nome do escolhido.
# ------------------------------------------------------------------------
from random import choice
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
escolha = choice([n1, n2, n3, n4])
print(f'Escolhido: {escolha}')
