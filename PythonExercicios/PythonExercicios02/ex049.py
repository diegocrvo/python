"""Refaça o desafio 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando um laço for.
-----------------------------------------------------------------------------------"""
n = int(input('\033[36mDigite um número: \033[m'))

print('\033[33m-\033[m' * 20)
print(f'   \033[46;1mTABUADA DE {n}\033[m')
print('\033[33m-\033[m' * 20, '\n')

for c in range(1, 11):
    r = n * c
    if c % 2 == 1:
        print(f'   \033[7m{n} X {c:2} = {r:3}\033[m')
    else:
        print(f'   {n} X {c:2} = {r:3}')

print('')
print('\033[33m-\033[m' * 20)
