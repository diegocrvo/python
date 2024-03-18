"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela."""

list = []
for c in range(0, 5):
    value = (int(input('Digite um número: ')))
    if c == 0 or value > list[-1]:
        list.append(value)
    else:
        pos = 0
        while pos < len(list):
            if value <= list[pos]:
                list.insert(pos, value)
                break
            pos += 1
print(f'Os valores digitados em ordem foram {list}.')
