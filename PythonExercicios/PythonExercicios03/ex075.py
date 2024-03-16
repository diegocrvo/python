"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o valor 3.
C) Quais foram os números pares.
------------------------------------------------------------------------------------"""
num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))

print(f'Você digitou os valores {num}.'
      f'\nO valor 9 apareceu {num.count(9)} veze(s).')
if 3 in num:
    print(f'O valor 3 foi digitado na {num.index(3) + 1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitado(s) foi(ram)', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
