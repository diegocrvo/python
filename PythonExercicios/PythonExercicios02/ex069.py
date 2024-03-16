"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
---------------------------------------------------------------------------------------------"""
maior18 = feminino_menos20 = masculino = 0
while True:
    idade = int(input('Qual a idade? '))
    if idade >= 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]? ')).strip().upper()[0]
    if sexo == 'M':
        masculino += 1
    if sexo == 'F' and idade < 20:
        feminino_menos20 += 1
    continuar = ' '
    print('-' * 40)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
        print('-' * 40)
    if continuar == 'N':
        break
print(f'Foram cadastrado(s) {maior18} pessoa(s) maior(es) de 18 anos.')
print(f'Foram cadastrado(s) {masculino} pessoa(s) do sexo masculino.')
print(f'Foram cadastrado(s) {feminino_menos20} pessoa(s) com menos de 20 anos do sexo feminino.')
print('\033[31mPrograma Encerrado.\033[m')
