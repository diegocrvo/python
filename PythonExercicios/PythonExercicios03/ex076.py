"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
----------------------------------------------------------------------------------"""
produtos = ('Refrigerante', 5.00,
            'Arroz', 4.50,
            'Margarina', 2.50,
            'Biscoito', 2.89)
print('-' * 40)
print(f'{"LISTA DE PRODUTOS E PREÇOS":^40}')
print('-' * 40)
for position in range(0, len(produtos)):
    if position % 2 == 0:
        print(f'{produtos[position]:.<30}', end='')
    else:
        print(f'R${produtos[position]:>6.2f}')
print('-' * 40)
