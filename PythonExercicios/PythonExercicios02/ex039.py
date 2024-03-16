"""Faça um programa qua leia o ano de nascimento de um jovem e informe,
conforme a sua idade:
- Se ele ainda vai se alistar no serviço militar.
- Se é a hora de alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
-------------------------------------------------------------------------------"""
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
opção = int(input('''Qual seu sexo:
[ 1 ] - Masculino
[ 2 ] - Feminino
Digite 1 ou 2: '''))
if opção == 1:
    print(f'Você faz {idade} anos esse ano.')
    if idade < 18:
        saldo = 18 - idade
        print(f'\033[32mVocê ainda irá se alistar no serviço militar, falta(m) {saldo} ano(s).')
        print(f'Você deve se alistar no ano {atual + saldo}.')
    elif idade > 18:
        saldo = idade - 18
        print(f'\033[31mVocê já deveria ter se alistado no serviço militar há {saldo} ano(s).')
        print(f'Você deveria ter se alistado no ano {atual - saldo}.')
    else:
        print('\033[33mEste ano você deverá se alistar no serviço militar.')
elif opção == 2:
    print('O Serviço Militar não é obrigatório para você.')
else:
    print('\033[31mEntrada Inválida.')
