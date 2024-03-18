"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

list = list()
while True:
    list.append(int(input('Digite um número: ')))
    comand = str(input('Deseja continuar?[S/N]: '))
    if comand in 'Nn':
        break
list.sort(reverse=True)
print(f'Foram digitados {len(list)} números.')
print(f'Os valores digitados em ordem decrescente foram {list}')
if 5 in list:
    print('O valor 5 se encontra na lista.')
else:
    print('O valor 5 não se encontra na lista.')
