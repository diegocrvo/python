# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada.
n = int(input('\033[36mDigite um número: \033[m'))

print('\033[33m-\033[m' * 20)
print(f'   \033[46;1mTABUADA DE {n}\033[m')
print('\033[33m-\033[m' * 20)

print(f'''
    \033[7m{n} X {1:2} = {n * 1:3}\033[m
    {n} X {2:2} = {n * 2:3}
    \033[7m{n} X {3:2} = {n * 3:3}\033[m
    {n} X {4:2} = {n * 4:3}
    \033[7m{n} X {5:2} = {n * 5:3}\033[m
    {n} X {6:2} = {n * 6:3}
    \033[7m{n} X {7:2} = {n * 7:3}\033[m
    {n} X {8:2} = {n * 8:3}
    \033[7m{n} X {9:2} = {n * 9:3}\033[m
    {n} X {10} = {n * 10:3}
''')

print('\033[33m-\033[m' * 20)
