# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.
pp = float(input('Preço do produto: R$'))
print(f'Valor com desconto de 5%:  R${pp - (pp * 5) / 100}')
