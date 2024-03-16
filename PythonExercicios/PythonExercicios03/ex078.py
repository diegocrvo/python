"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista."""

num =list()
maior = 0
menor = 0
for count in range(0, 5):
    num.append(int(input(f'Digite um valor na posição {count+1}: ')))
    if count == 0:
        maior = menor = num[count]
    else:
        if num[count] > maior:
            maior = num[count]
        if num[count] < menor:
            menor = num[count]
print(f'Os valores digitados foram {num}.')
print(f'O maior valor digitado foi(ram) {maior}, na(s) posição(ões) ', end='')
for p, v in enumerate(num):
    if v == maior:
        print(f'{p+1}...', end=' ')
print(f'\nO menor valor digitado foi(ram) {menor}, na(s) posição(ões) ', end='')
for p, v in enumerate(num):
    if v == menor:
        print(f'{p+1}...', end=' ')
