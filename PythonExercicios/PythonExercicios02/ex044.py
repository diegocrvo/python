"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
----------------------------------------------------------------------------------"""
print('')
print(f'{" LOJAS CARVALHO ":=^40}\n')

valor = float(input('Digite o valor total em R$: '))
forma_pagamento = int(input('''\033[4mQual a forma pagamento?\033[m'
 
Formas de pagamento:

[ 1 ] - à vista dinheiro/cheque.
[ 2 ] - à vista no cartão.
[ 3 ] - em até 2x no cartão.
[ 4 ] - em 3x ou mais no cartão.

Digite a opção escolhida: '''))

price = valor

if forma_pagamento == 1:
    price = valor - (valor * 0.1)

elif forma_pagamento == 2:
    price = valor - (valor * 0.05)

elif forma_pagamento == 3:
    valor_parcela = valor / 2
    print(f'Dividido em 2X, o valor da parcela fica R${valor_parcela:.2f}')
    price = valor

elif forma_pagamento == 4:
    parcela = int(input('Quantas parcelas?: '))

    if parcela >= 3:
        price = valor + (valor * 0.2)
        valor_parcela = price / parcela
        print(f'Dividido em {parcela}X, o valor da parcela fica R${valor_parcela:.2f}')

    else:
        print('\033[31mEntrada Inválida.\033[m')

else:
    print('\033[31mEntrada inválida.\033[m')

print(f'Sua compra no valor de R${valor:.2f} vai custar R${price:.2f}.')
