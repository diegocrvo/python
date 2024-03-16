"""(FAÇA ESSE EXERCÍCIO COM "while" E DEPOIS COM "for")
Faça um programa que leia um número qualquer e mostre o seu fatorial.
ex.: 5!= 5x4x3x2x1 = 120
-----------------------------------------------------------------------------------"""

print('-' * 30)
print('FATORIAL'.center(30))
print('-' * 30)
print('Digite um número abaixo para \n'
      'saber seu fatorial.')
print('-' * 30)

n = int(input('Digite o número: '))
c = n
f = 1
print(f'\n{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
