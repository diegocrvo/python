"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, será
exibido todos os valores únicos digitados, em ordem crescente."""

values = list()
while True:
    values.append(int(input('Digite um valor: ')))
    if values[-1] in values[:-2]:
        del(values[-1])
        print('O valor foi duplicado, não será adicionado...')
    comando = str(input('Deseja continuar?[S/N]: '))
    if comando in 'nN':
        break
print(f'Você digitou os valores {sorted(values)}.')
